import sys
from pathlib import Path

import random

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ctrlr import seeded


def test_seeded_same_seed_deterministic() -> None:
    with seeded(123):
        a = [random.random() for _ in range(3)]
    with seeded(123):
        b = [random.random() for _ in range(3)]
    assert a == b


def test_seeded_different_seed_changes() -> None:
    with seeded(123):
        a = [random.random() for _ in range(3)]
    with seeded(124):
        b = [random.random() for _ in range(3)]
    assert a != b


def test_seeded_restores_state() -> None:
    random.seed(999)
    with seeded(123):
        _ = random.random()
    after = random.random()
    random.seed(999)
    expected_after = random.random()
    assert after == expected_after


def test_seeded_nested_contexts() -> None:
    with seeded(1):
        a = random.random()
        with seeded(2):
            b = random.random()
        c = random.random()
    with seeded(1):
        a2 = random.random()
        with seeded(2):
            b2 = random.random()
        c2 = random.random()
    assert a == a2
    assert b == b2
    assert c == c2


def test_seeded_string_and_bytes() -> None:
    with seeded("alpha"):
        a = random.random()
    with seeded(b"alpha"):
        b = random.random()
    assert a == b
