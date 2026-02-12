from __future__ import annotations

import random

import pytest

from oracle_api.control import CtrlrError
from oracle_api.seeded import seeded
from oracle_tools.budget import budget


def test_budget_consume_and_remaining():
    b = budget(2, label="demo")
    assert b.remaining == 2
    b.consume()
    assert b.used == 1
    assert b.remaining == 1


def test_budget_exceeded_raises():
    b = budget(1)
    b.consume()
    with pytest.raises(CtrlrError):
        b.consume()


def test_seeded_restores_state():
    state_before = random.getstate()
    with seeded(123):
        first = random.random()
        second = random.random()
    assert random.getstate() == state_before
    with seeded(123):
        assert random.random() == first
        assert random.random() == second
