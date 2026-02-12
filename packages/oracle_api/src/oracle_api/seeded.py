from __future__ import annotations

import random
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def seeded(seed: int) -> Iterator[int]:
    """Temporarily set the global random seed and restore the prior RNG state."""
    state = random.getstate()
    random.seed(seed)
    try:
        yield seed
    finally:
        random.setstate(state)
