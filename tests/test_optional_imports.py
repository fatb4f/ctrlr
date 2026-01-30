import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import ctrlr


def test_minimal_import_ctrlr() -> None:
    assert hasattr(ctrlr, "__all__")


def test_optional_import_error_message() -> None:
    with pytest.raises(ImportError) as excinfo:
        ctrlr.optional_import("definitely_missing_pkg_123", "test")
    msg = str(excinfo.value)
    assert "ctrlr[test]" in msg
