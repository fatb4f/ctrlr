from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ORACLE_SRC = ROOT / "packages" / "oracle" / "src"
if str(ORACLE_SRC) not in sys.path:
    sys.path.insert(0, str(ORACLE_SRC))


def test_imports_smoke() -> None:
    import oracle

    assert hasattr(oracle, "OTelRuntime")
