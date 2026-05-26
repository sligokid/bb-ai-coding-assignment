## Parent PRD

`issues/prd.md`

## What to build

Implement `calculate_average_price(properties, street_names)` in `trees.py` — filters the property list to rows whose `Street Name` is in the supplied set, parses prices, and returns the arithmetic mean as a float. Raises `ValueError` if no rows match.

Write the corresponding unit tests in `test_trees.py`:
- `test_calculate_average_price` — asserts the correct average is returned for a small inline dataset
- `test_calculate_average_price_no_matches` — asserts `ValueError` is raised when no streets match

Implement `main.py` as the CLI entry point: accepts two positional arguments (trees JSON path, property CSV path), calls the library functions, and prints two labelled output lines formatted with euro sign and two decimal places.

See the "Average calculation" and "Entry point" entries in the Implementation Decisions section of the PRD for exact interfaces and output format.

## Acceptance criteria

- [ ] `calculate_average_price(properties, street_names)` returns the correct float average
- [ ] Street name lookup uses a `set` (not a list) for O(1) membership testing
- [ ] `calculate_average_price` raises `ValueError("No matching properties found")` when the filtered list is empty
- [ ] `test_calculate_average_price` and `test_calculate_average_price_no_matches` both pass with inline data
- [ ] `main.py` accepts exactly two positional CLI arguments (no hardcoded paths)
- [ ] `main.py` prints two lines, e.g. `Average property price on streets with tall trees:  €450,123.45`
- [ ] Output formatting (euro sign, comma separators, 2 decimal places) lives in `main.py`, not `trees.py`
- [ ] Program requires no user interaction after launch

## Blocked by

- Blocked by `issues/001-parse-trees-json.md`
- Blocked by `issues/002-parse-property-csv.md`

## User stories addressed

- User story 1
- User story 2
- User story 3
- User story 4
- User story 8
- User story 9
- User story 11
- User story 12
- User story 13
