# Week 5 - Findings

## 1. Ruff Results

Ruff reported:

`All checks passed!`

No Ruff violations were detected with the current configuration.

## 2. Pylint Results

Pylint rated the code **5.62/10**.

The following issues were found:

| Code | Finding | Explanation |
|---|---|---|
| C0304 | Missing final newline | Files do not end with a newline. |
| C0114 | Missing module docstring | The modules have no descriptions. |
| C0116 | Missing function docstring | Functions have no descriptions. |
| R1705 | No-else-return | An elif after return is unnecessary. |

## 3. Extra Code Smells

- Missing documentation makes the code harder to understand.
- Repeated test structure can make tests longer.
- The grading function uses multiple conditional branches.

## 4. Hidden Bug Explanation

No confirmed hidden bug has been identified yet. Further characterization and boundary testing are needed to identify unexpected behavior.