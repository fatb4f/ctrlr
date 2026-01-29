from __future__ import annotations

import contextlib
import hashlib
import random
from typing import Iterator


def _seed_to_int(seed: int | str | bytes) -> int:
    if isinstance(seed, int):
        return seed
    if isinstance(seed, str):
        seed_bytes = seed.encode("utf-8")
    else:
        seed_bytes = seed
    digest = hashlib.sha256(seed_bytes).digest()
    return int.from_bytes(digest, "big")


@contextlib.contextmanager
def seeded(seed: int | str | bytes) -> Iterator[None]:
    """Temporarily seed RNGs and restore their state on exit."""
    seed_int = _seed_to_int(seed)
    py_state = random.getstate()
    np_state = None
    np = None

    try:
        random.seed(seed_int)
        try:
            import numpy as np  # type: ignore

            np_state = np.random.get_state()
            np.random.seed(seed_int)
        except Exception:
            np = None
        yield
    finally:
        random.setstate(py_state)
        if np_state is not None and np is not None:
            np.random.set_state(np_state)
