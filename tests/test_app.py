import sys
from pathlib import Path
import math
import pytest

# Add <repo>/src to the import path so we can "import app"
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from app import add, sub, mul, div, log, square, sin, cos, sqrt, percent


# -----------------
# Basic operations
# -----------------

@pytest.mark.parametrize(
    "a,b,expected",
    [(5, 6, 11), (0, 0, 0), (-5, 6, 1), (1.5, 2.5, 4.0)],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(10, 3, 7), (0, 5, -5), (-5, -6, 1), (2.5, 1.0, 1.5)],
)
def test_sub(a, b, expected):
    assert sub(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(3, 4, 12), (0, 999, 0), (-3, 4, -12), (2.5, 2, 5.0)],
)
def test_mul(a, b, expected):
    assert mul(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(10, 2, 5), (5, 2, 2.5), (-9, 3, -3), (0, 5, 0)],
)
def test_div(a, b, expected):
    assert div(a, b) == expected


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


# -----------------
# Advanced operations
# -----------------

@pytest.mark.parametrize(
    "x,base,expected",
    [(100, 10, 2), (8, 2, 3), (math.e, math.e, 1)],
)
def test_log_valid(x, base, expected):
    assert log(x, base) == pytest.approx(expected)


@pytest.mark.parametrize(
    "x,base",
    [(0, 10), (-1, 10), (10, 1), (10, 0), (10, -2)],
)
def test_log_invalid(x, base):
    with pytest.raises(ValueError):
        log(x, base)


@pytest.mark.parametrize(
    "x,expected",
    [(0, 0), (3, 9), (-3, 9), (2.5, 6.25)],
)
def test_square(x, expected):
    assert square(x) == expected


def test_sin():
    assert sin(0) == pytest.approx(0)
    assert sin(math.pi / 2) == pytest.approx(1)


def test_cos():
    assert cos(0) == pytest.approx(1)
    assert cos(math.pi) == pytest.approx(-1)


@pytest.mark.parametrize(
    "x,expected",
    [(0, 0), (4, 2), (2.25, 1.5)],
)
def test_sqrt(x, expected):
    assert sqrt(x) == pytest.approx(expected)


def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)


@pytest.mark.parametrize(
    "x,expected",
    [(0, 0), (50, 0.5), (12.5, 0.125), (-10, -0.1)],
)
def test_percent(x, expected):
    assert percent(x) == pytest.approx(expected)
