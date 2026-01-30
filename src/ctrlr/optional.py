from __future__ import annotations

from importlib import import_module


def optional_import(module: str, extra: str) -> object:
    """Import an optional dependency or raise a helpful error."""
    try:
        return import_module(module)
    except Exception as exc:  # ImportError or runtime import failure
        raise ImportError(
            f"Optional dependency '{module}' is required. Install with `pip install ctrlr[{extra}]`."
        ) from exc
