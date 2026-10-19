
import math
from triangle import is_valid_triangle, classify_triangle


def test_invalid_zero_side():
    assert is_valid_triangle(0, 4, 5) is False
    assert classify_triangle(0, 4, 5) == "Invalid"


def test_invalid_negative_side():
    assert classify_triangle(-1, 4, 5) == "Invalid"


def test_invalid_triangle_inequality():
    assert classify_triangle(1, 2, 4) == "Invalid"


def test_degenerate_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 6) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_triangle_non_integer():
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hypotenuse) == "Right Isosceles"


def test_right_triangle_permutations():
    assert classify_triangle(5, 3, 4) == "Right Scalene"
    assert classify_triangle(4, 5, 3) == "Right Scalene"
