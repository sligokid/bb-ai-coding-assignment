# PRD: Do More Trees Mean More Money?

## Problem Statement

A developer needs to determine whether residential properties on streets with tall trees sell for more, on average, than properties on streets with short trees in Dublin. Two datasets are available: a nested JSON file categorising Dublin streets by tree height (short vs tall, based on Dublin City Council median tree height data), and a CSV extract of the Residential Property Price Register containing property addresses, street names, and sale prices. The program must join these datasets and compute the two average prices without any user interaction at runtime.

## Solution

A small, production-quality Python library and CLI entry point that:
1. Loads and recursively parses the trees JSON to extract street name sets for each height category.
2. Loads and parses the property price CSV.
3. Joins on the `Street Name` column and computes the average sale price for each category.
4. Prints the two averages to stdout.

The code is packaged as a zip file with a README, is covered by unit tests, and has no runtime dependencies beyond the Python standard library.

## User Stories

1. As a developer running the program, I want to pass the data file paths as CLI arguments so that I can point the program at any copy of the files without editing code.
2. As a developer running the program, I want the program to require no user interaction after it starts so that it can be invoked as part of a larger automated pipeline.
3. As a developer reading the output, I want to see the average price for tall-tree streets and the average price for short-tree streets on separate labelled lines so that the result is immediately clear.
4. As a developer reading the output, I want prices formatted with a euro sign and two decimal places so that the numbers are easy to read.
5. As a developer importing the library, I want a function that extracts street names from the nested JSON structure so that I can reuse just that logic in other contexts.
6. As a developer importing the library, I want the JSON extraction to handle arbitrarily deep nesting so that the function is robust to structural changes in the source data.
7. As a developer importing the library, I want a function that parses a price string (e.g. `€79,500.00`) into a float so that the parsing logic is isolated and testable.
8. As a developer importing the library, I want a function that calculates the average price for a given set of street names so that the join and aggregation logic is isolated and testable.
9. As a developer using the library, I want a `ValueError` raised when no properties match the supplied street names so that I get a clear signal rather than a silent zero or NaN.
10. As a developer using the library, I want file I/O errors to propagate naturally (e.g. `FileNotFoundError`) so that error messages are clear and actionable without extra wrapping.
11. As a developer running the test suite, I want all tests to use inline data so that tests run without access to the real data files.
12. As a developer reviewing the code, I want all functions to have a single, well-defined responsibility so that the code is easy to reason about and maintain.
13. As a developer reviewing the code, I want functions and variables named descriptively (e.g. `parse_price`, not `process`) so that intent is clear without reading the implementation.
14. As a new developer onboarding to the project, I want a README with setup, run, and test instructions so that I can get the program working without asking anyone.
15. As a new developer onboarding to the project, I want to know the minimum Python version required so that I can set up my environment correctly.
16. As a developer receiving the submission, I want a single zip file containing all source files and the README so that unpacking it gives me everything I need.

## Implementation Decisions

- **Three files:** `trees.py` (all business logic), `main.py` (CLI entry point), `test_trees.py` (unit tests). No packages, no subdirectories.
- **JSON parsing:** A recursive generator function `extract_street_names(node)` that yields a key when its value is an integer (a leaf/height value) and recurses when its value is a dict. Called separately for `data["short"]` and `data["tall"]` to produce two sets.
- **CSV parsing:** stdlib `csv.DictReader` with `utf-8-sig` encoding (handles potential BOM). Returns a list of row dicts.
- **Price parsing:** `parse_price(price_str)` strips `€` and `,` then calls `float()`. Raises `ValueError` naturally on malformed input.
- **Average calculation:** `calculate_average_price(properties, street_names)` where `street_names` is a `set` for O(1) lookup. Filters rows by `row["Street Name"] in street_names`, parses prices, computes `sum / len`. Raises `ValueError` if the filtered list is empty.
- **Entry point:** `main.py` accepts two positional CLI arguments (trees JSON path, property CSV path) and prints two labelled output lines. Formatting (euro sign, comma separators, 2 decimal places) is handled in `main.py`, not in `trees.py`.
- **No runtime dependencies:** stdlib only. `pytest` is the sole dev dependency.
- **Python version:** 3.10+ (uses built-in generic type hints like `list[str]`, `set[str]`).

## Testing Decisions

A good test verifies observable, external behaviour of a function given controlled inputs — not how the function is implemented internally. Tests should not require real data files, network access, or subprocess calls.

**Modules to test:** `trees.py` exclusively. `main.py` is not unit-tested (it is a thin CLI wrapper).

**Tests to write:**

1. `test_extract_street_names` — given a small hand-crafted nested dict, asserts the correct set of street name strings is returned.
2. `test_parse_price_valid` — given `"€79,500.00"`, asserts the result is `79500.0`.
3. `test_parse_price_invalid` — given a malformed string, asserts `ValueError` is raised.
4. `test_calculate_average_price` — given a small list of property row dicts and a matching street name set, asserts the correct average float is returned.
5. `test_calculate_average_price_no_matches` — given a street name set with no matching rows, asserts `ValueError` is raised.

All tests use inline data defined in the test body. No fixtures, no temp files, no mocking.

## Out of Scope

- HTML, web, or graphical presentation of results.
- Container configuration (Docker, etc.).
- CI/CD pipelines.
- Downloading the data files programmatically (files are passed as CLI arguments).
- Statistical analysis beyond simple arithmetic mean (median, percentiles, etc.).
- Handling properties that appear on both a short-tree and a tall-tree street (the brief states street names are unique to one category).
- Scaling to large datasets (no streaming, chunking, or database storage needed).
- Internationalisation or currency conversion.

## Further Notes

- The brief explicitly states the street names in `dublin-trees.json` exactly match the `Street Name` column in `dublin-property.csv` — no fuzzy matching or normalisation is required.
- Only the leaf entries in the JSON (those with an integer value) represent street names. Intermediate keys are structural and must be ignored.
- The brief discourages "enterprisey" complexity. The architecture should match the simplicity of the problem.
- Recommended reading from the brief: "A Guide to Naming Variables" and "Cognitive load is what matters" — both inform the naming and structural decisions above.
