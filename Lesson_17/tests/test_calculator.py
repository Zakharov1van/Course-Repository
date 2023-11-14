import pytest
from src import calculator


@pytest.mark.parametrize("a, b, c", [(1, 2, 3), (10, 20, 30), ("a", "b", "Arguments should be numeric.")])
def test_adding(a, b, c):
    assert calculator.add(a, b) == c


@pytest.mark.parametrize("a, b, c", [(3, 2, 1), (30, 20, 10), ("a", "b", "Arguments should be numeric.")])
def test_subtracting(a, b, c):
    assert calculator.subtract(a, b) == c


@pytest.mark.parametrize("a, b, c", [(1, 2, 2), (10, 20, 200), ("a", "b", "Arguments should be numeric.")])
def test_multiplying(a, b, c):
    assert calculator.multiply(a, b) == c


@pytest.mark.parametrize("a, b, c", [(4, 2, 2), (100, 50, 2), (30, 0, "Can't divide by 0."),
                                     ("a", "b", "Arguments should be numeric.")])
def test_dividing(a, b, c):
    assert calculator.divide(a, b) == c


@pytest.mark.parametrize("a, b", [(16, 4), (64, 8), (-100, "Can't take square root of a negative number"),
                                  ("a", "Argument should be numeric.")])
def test_square_root(a, b):
    assert calculator.square_root(a) == b
