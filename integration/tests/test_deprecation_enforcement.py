from __future__ import annotations

import ast
import re
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEGACY_MODULES = {"oracle_api", "oracle_tools"}
TARGET_CODE_ROOTS = [
    ROOT / "packages" / "oracle" / "src",
    ROOT / "integration" / "tests",
]
SCAN_DOC_ROOTS = [ROOT / "README.md", ROOT / "docs"]
PRIMARY_DOC_BANNED_PATTERNS = (
    "pip install -e packages/oracle_api",
    "pip install -e packages/oracle_tools",
    "from oracle_api import",
    "from oracle_tools import",
    "import oracle_api",
    "import oracle_tools",
)


def _iter_python_files() -> list[Path]:
    out: list[Path] = []
    for root in TARGET_CODE_ROOTS:
        if root.is_file() and root.suffix == ".py":
            out.append(root)
            continue
        if root.is_dir():
            out.extend(sorted(root.rglob("*.py")))
    return out


def _iter_markdown_files() -> list[Path]:
    out: list[Path] = []
    for root in SCAN_DOC_ROOTS:
        if root.is_file():
            out.append(root)
            continue
        out.extend(sorted(root.rglob("*.md")))
    return out


def _normalize_dep_name(raw: str) -> str:
    candidate = raw.strip().lower()
    candidate = re.split(r"[<>=!~;\[]", candidate, maxsplit=1)[0]
    return candidate.replace("_", "-")


def _find_legacy_imports_in_source(source: str, *, path: Path) -> list[str]:
    tree = ast.parse(source, filename=str(path))
    findings: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".", 1)[0]
                if top in LEGACY_MODULES:
                    findings.append(f"{path}:{node.lineno} import {alias.name}")
        elif isinstance(node, ast.ImportFrom) and node.module:
            top = node.module.split(".", 1)[0]
            if top in LEGACY_MODULES:
                findings.append(f"{path}:{node.lineno} from {node.module}")
    return findings


def test_import_gate_rejects_legacy_runtime_and_test_imports() -> None:
    violations: list[str] = []
    for file_path in _iter_python_files():
        source = file_path.read_text(encoding="utf-8")
        violations.extend(_find_legacy_imports_in_source(source, path=file_path))
    assert not violations, "legacy import gate violations:\n" + "\n".join(sorted(violations))


def test_import_gate_detection_has_regression_fixture() -> None:
    sample = "\n".join(
        [
            "import os",
            "import oracle_api",
            "from oracle_tools.budget import budget",
        ]
    )
    findings = _find_legacy_imports_in_source(sample, path=Path("synthetic_fixture.py"))
    assert len(findings) == 2
    assert any("import oracle_api" in item for item in findings)
    assert any("from oracle_tools.budget" in item for item in findings)


def test_dependency_gate_rejects_legacy_workspace_wiring() -> None:
    root_pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    members = root_pyproject["tool"]["uv"]["workspace"]["members"]
    assert not any(member in {"packages/oracle_api", "packages/oracle_tools"} for member in members)

    oracle_pkg = tomllib.loads((ROOT / "packages" / "oracle" / "pyproject.toml").read_text(encoding="utf-8"))
    deps: list[str] = []
    deps.extend(oracle_pkg.get("project", {}).get("dependencies", []))
    opt = oracle_pkg.get("project", {}).get("optional-dependencies", {})
    for values in opt.values():
        deps.extend(values)

    normalized = [_normalize_dep_name(dep) for dep in deps]
    assert "oracle-api" not in normalized
    assert "oracle-tools" not in normalized


def test_docs_gate_rejects_legacy_primary_recommendations() -> None:
    violations: list[str] = []
    for file_path in _iter_markdown_files():
        rel = file_path.relative_to(ROOT).as_posix()
        if rel.startswith("docs/otel_migration/"):
            # Migration docs intentionally inventory legacy references.
            continue
        text = file_path.read_text(encoding="utf-8")
        low = text.lower()
        for pattern in PRIMARY_DOC_BANNED_PATTERNS:
            if pattern in low:
                violations.append(f"{file_path}: contains forbidden primary pattern '{pattern}'")
    assert not violations, "legacy docs gate violations:\n" + "\n".join(sorted(violations))


def test_docs_legacy_mentions_are_explicitly_deprecated() -> None:
    violations: list[str] = []
    for file_path in _iter_markdown_files():
        text = file_path.read_text(encoding="utf-8")
        low = text.lower()
        mentions_legacy = "oracle_api" in low or "oracle_tools" in low
        if mentions_legacy and "deprecat" not in low:
            violations.append(f"{file_path}: mentions legacy package without deprecation label")
    assert not violations, "legacy docs labeling violations:\n" + "\n".join(sorted(violations))
