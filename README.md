# Triangle Classifier — CSC 325

## Project Description

The Triangle Classifier is a Python program that determines whether three given side lengths form a valid triangle. If the triangle is valid, the program classifies it as Equilateral, Isosceles, or Scalene.

The program also identifies right triangles using the Pythagorean theorem. Floating-point tolerance is used to ensure accurate classification when working with decimal side lengths.

The project includes unit tests using pytest and an acceptance test based on the requirements of a stained-glass studio.

## Project Files

- `triangle.py` — Implements triangle validation and classification.
- `test_triangle.py` — Contains 10 unit tests covering the classification requirements.
- `test_acceptance.py` — Contains the customer acceptance test.
- `requirements.txt` — Lists pytest as the testing dependency.
- `README.md` — Contains project documentation, test instructions, and AI-use disclosure.

## How to Run the Tests

1. Install Python 3.
2. Download or clone the GitHub repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Install the required dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Run all tests:

   ```bash
   python -m pytest -v
   ```

If the `python` command is unavailable on Windows, the Python launcher may be used instead:

```bash
py -m pytest -v
```

### Test Results

The project was tested locally using Python 3.12 and pytest.

| Test Category | Tests Passed |
|---|---|
| Unit Tests | 10 |
| Acceptance Tests | 1 |
| Total | 11 |

All 11 tests passed successfully.

## Triangle Classification Rules

| Condition | Expected Result |
|---|---|
| Any side is zero or negative | Invalid |
| Triangle inequality fails | Invalid |
| Sum of two sides equals the third | Invalid |
| All three sides equal | Equilateral |
| Exactly two sides equal | Isosceles |
| All three sides different | Scalene |
| Valid right triangle with three different sides | Right Scalene |
| Valid right triangle with exactly two equal sides | Right Isosceles |

### Why an Equilateral Triangle Cannot Be Right

An equilateral triangle has three equal interior angles of 60 degrees. A right triangle must contain a 90-degree angle, so an equilateral triangle cannot also be a right triangle.

## Equivalence Classes and Boundaries

The following equivalence classes were identified:

1. Invalid triangles containing zero-length sides.
2. Invalid triangles containing negative side lengths.
3. Invalid triangles that violate the triangle inequality.
4. Degenerate triangles where the sum of two sides equals the third.
5. Valid equilateral triangles.
6. Valid isosceles triangles.
7. Valid scalene triangles.
8. Valid right triangles with integer side lengths.
9. Valid right triangles with non-integer side lengths.

### Boundary Test Cases

| Input | Expected Result | Reason |
|---|---|---|
| (0, 4, 5) | Invalid | Zero-length side |
| (-1, 4, 5) | Invalid | Negative side |
| (1, 2, 3) | Invalid | Degenerate triangle |
| (1, 2, 4) | Invalid | Triangle inequality violation |
| (5, 5, 5) | Equilateral | All sides equal |
| (5, 5, 6) | Isosceles | Exactly two sides equal |
| (4, 5, 6) | Scalene | All sides different |
| (3, 4, 5) | Right Scalene | Satisfies the Pythagorean theorem |
| (5, 5, 5 * sqrt(2)) | Right Isosceles | Tests floating-point tolerance |

## Copilot Review Log

GitHub Copilot autocomplete was used in Visual Studio Code to assist with drafting unit tests for the triangle classifier. Each suggestion was reviewed against the assignment requirements before being accepted, edited, or rejected.

| Test | Copilot-suggested? | Decision | Why |
|---|---|---|---|
| test_equilateral_triangle | Yes | Kept | Copilot correctly tested that three equal sides return "Equilateral". |
| test_degenerate_triangle | Yes | Kept | Copilot correctly included the degenerate case (1, 2, 3), which must return "Invalid". |
| test_invalid_zero_side | Yes | Kept | Copilot correctly included zero and negative side-length cases. |
| test_isosceles_triangle | Yes | Kept | Copilot correctly checked that exactly two equal sides produce "Isosceles". |
| test_scalene_triangle | Yes | Kept | Copilot correctly tested a valid triangle with three different side lengths. |
| test_right_scalene_triangle | Yes | Kept | Copilot correctly tested the 3-4-5 right triangle and suggested testing different side orders. |
| test_right_triangle_non_integer | Yes | Kept | Copilot correctly suggested a square
Copilot Suggestion Review

One issue identified in the generated code was the placeholder module import:

from your_module import classify_triangle

The actual project uses a file named triangle.py, so the correct import is:

from triangle import classify_triangle

Using the placeholder import unchanged would result in a module import error.

Copilot also suggested additional large-number tests. These were reviewed but not included in the final test suite because the required equivalence classes and boundary conditions were already covered.

For floating-point testing, Copilot correctly suggested using math.sqrt(2) rather than relying on hard-coded approximate values. The implementation uses math.isclose() to detect right triangles with floating-point side lengths.

Acceptance Criteria

The customer is a stained-glass studio that needs to determine whether glass pieces can be constructed from three side lengths and whether a right-angle piece requires reinforced corners.

Criterion 1 — Invalid Triangle Handling

Given three side lengths where any side is less than or equal to zero, or where the triangle inequality fails, the program must return "Invalid" without crashing.

Criterion 2 — Correct Shape Classification

Given three valid side lengths, the program must return "Equilateral" when all sides are equal, "Isosceles" when exactly two sides are equal, or "Scalene" when all sides are different, with the appropriate right-angle prefix when applicable.

Criterion 3 — Right-Angle Identification

Given three valid side lengths satisfying the Pythagorean theorem within the program's floating-point tolerance, the program must return a classification beginning with "Right " so the studio can identify pieces requiring reinforced corners.

Acceptance Testing

The acceptance test in test_acceptance.py checks the behavior of the classify_triangle() function using customer-facing scenarios.

The test verifies that:

Invalid side lengths return "Invalid" without raising an exception.

Valid triangles receive the correct shape classification.

Right-angle triangles receive the "Right " prefix.

The acceptance test passed when executed using pytest.



Tools Used

GitHub Copilot autocomplete was used in Visual Studio Code to assist with drafting unit tests. ChatGPT was used for implementation guidance, test development, documentation, and troubleshooting.

All generated code was reviewed against the assignment requirements, and the final test suite was verified using pytest.


Verification and Review

Copilot suggestions were compared against the triangle classification requirements. The final test suite was executed using pytest, with all 10 unit tests and 1 acceptance test passing.


The tests covered zero and negative side lengths, degenerate triangles, triangle inequality violations, Equilateral, Isosceles, Scalene, Right Scalene, and Right Isosceles classifications.

The non-integer right-triangle test used 5 * math.sqrt(2) to verify floating-point behavior. The implementation uses math.isclose() instead of direct floating-point equality for checking the Pythagorean theorem.

Copilot Usage

Github copilot was used accordinly when making this project work however some extra processes such as installing it when through some processes

Acceptance Test Assistance

### Part 3 — Acceptance Test Explanation

For Part 3, I focused on the stained-glass studio's needs rather than just testing individual functions. I chose three acceptance criteria: identifying invalid triangles, correctly classifying valid triangles, and detecting right angles.

I considered these important because the studio needs to know whether a glass piece can actually be constructed and whether its shape requires reinforced corners. I used these requirements to evaluate the program from the customer's perspective.

After preparing the acceptance test, I ran it using pytest to verify that the program met the expected requirements. The acceptance test passed successfully.