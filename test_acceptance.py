
from triangle import classify_triangle


def test_stained_glass_customer_requirements():
    # Invalid pieces must be identified without crashing.
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(0, 4, 5) == "Invalid"

    # Valid pieces must receive the correct shape.
    assert classify_triangle(6, 6, 6) == "Equilateral"
    assert classify_triangle(6, 6, 8) == "Isosceles"
    assert classify_triangle(4, 5, 6) == "Scalene"

    # Right-angle pieces must be flagged for reinforcement.
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * 2 ** 0.5) == "Right Isosceles"