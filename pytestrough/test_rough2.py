import pytest


def test_total_divisible_by_6(input_total):
    assert input_total % 5 == 0


def test_total_divisible_by_8(input_total):
    assert input_total % 9 == 0
