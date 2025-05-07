# Exemplary calculator tests
import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, expected ", [(4, 100), (10, 1010), (24, 11000), (100, 1100100)]
)
def test_to_binary(a, expected):
    result = utils.to_binary(a)
    assert result == expected


@pytest.mark.parametrize("a, expected ", [(-1, -1), (120, -1), (0, 0), (100, 1100100)])
def test_to_binary_range(a, expected):
    result = utils.to_binary(a)
    assert result == expected


@pytest.mark.parametrize("a, expected ", [(-20, -1), (-1, -1), (32.2, -1), (0.1, -1)])
def test_to_binary_natural(a, expected):
    result = utils.to_binary(a)
    assert result == expected
