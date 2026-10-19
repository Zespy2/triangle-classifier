# Triangle Classifier — CSC 325

## Project Description

This project is a Python triangle classifier that determines whether three given side lengths form a valid triangle. If valid, the program identifies the triangle as Equilateral, Isosceles, or Scalene. It also identifies right triangles using the Pythagorean theorem.

The project includes unit tests using pytest and an acceptance test based on customer requirements from a stained-glass studio.

## How to Run the Tests

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Install the required dependencies:

   `python -m pip install -r requirements.txt`

5. Run the tests:

   `python -m pytest -v`

## Triangle Classification Rules

| Condition | Expected Result |
|---|---|
| Any side is zero or negative | Invalid |
| Triangle inequality fails | Invalid |
| All three sides are equal | Equilateral |
| Exactly two sides are equal | Isosceles |
| All three sides are different | Scalene |
| Valid right triangle | Right Scalene or Right Isosceles |

### Why an Equilateral Triangle Cannot Be Right

An equilateral triangle has three equal angles of 60 degrees. A right triangle must contain a 90-degree angle, so an equilateral triangle cannot also be right.

## Equivalence Classes and Boundaries

The following equivalence classes were identified:

- Invalid triangles with zero or negative side lengths.
- Invalid triangles that violate the triangle inequality.
- Degenerate triangles where two sides sum exactly to the third.
- Valid equilateral triangles.
- Valid isosceles triangles.
- Valid scalene triangles.
- Valid right triangles.

Boundary cases include:

- `(0, 4, 5)` — Invalid because one side is zero.
- `(-1, 4, 5)` — Invalid because one side is negative.
- `(1, 2, 3)` — Invalid because the sum of two sides equals the third.
- `(1, 2, 4)` — Invalid because the triangle inequality fails.
- `(3, 4, 5)` — Right Scalene.
- `(5, 5, 5 * sqrt(2))` — Right Isosceles, requiring floating-point tolerance.

## Copilot Review Log

GitHub Copilot was used to help generate and review unit test suggestions. Each suggestion must be evaluated against the assignment requirements rather than only the current implementation.

**Complete this table using the suggestions you actually received.**

| Test | Copilot-suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|
| test_equilateral_triangle | [Yes/No] | [Decision] | [What was checked] |
| test_degenerate_triangle | [Yes/No] | [Decision] | [What was checked] |
| test_right_triangle_non_integer | [Yes/No] | [Decision] | [What was checked] |
| test_invalid_zero_side | [Yes/No] | [Decision] | [What was checked] |

At least one row should document a specific mistake or omission you actually identified and corrected.

## Acceptance Criteria

The stained-glass studio requires accurate triangle classification to prevent incorrectly shaped glass pieces from being produced.

**Criterion 1 — Invalid Triangles**

Given three side lengths that do not form a valid triangle, the classifier must return `"Invalid"` without raising an exception.

**Criterion 2 — Valid Triangle Classification**

Given three positive side lengths satisfying the triangle inequality, the classifier must return the correct classification: `"Equilateral"`, `"Isosceles"`, or `"Scalene"`, with the right-angle prefix when applicable.

**Criterion 3 — Right-Angle Identification**

Given side lengths satisfying the Pythagorean theorem within the specified floating-point tolerance, the classifier must return a classification beginning with `"Right "` so the studio can identify pieces requiring reinforced corners.

## Acceptance Testing

The acceptance test in `test_acceptance.py` checks customer-facing behavior by calling `classify_triangle()` with representative valid, invalid, and right-angle side lengths.

The acceptance test should be developed independently without GitHub Copilot, as required by the assignment.

## AI-Use Disclosure

AI tools used: [List the tools actually used, such as ChatGPT and GitHub Copilot Chat.]

Purpose: [Describe which code, test suggestions, explanations, or documentation each tool helped with.]

Verification: [Describe the test cases you personally checked, corrections made, and pytest results.]

GitHub Copilot autocomplete usage: [State whether autocomplete was used. If only Copilot Chat was used, state that accurately.]

The acceptance criteria and acceptance test are required to be completed without Copilot assistance.i