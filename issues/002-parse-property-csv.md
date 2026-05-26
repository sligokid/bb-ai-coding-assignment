## Parent PRD

`issues/prd.md`

## What to build

Implement two functions in `trees.py`:
- `load_properties(filepath)` — reads the CSV using `csv.DictReader` with `utf-8-sig` encoding and returns a list of row dicts
- `parse_price(price_str)` — strips the `€` prefix and comma thousand-separators and returns a `float`

Write the corresponding unit tests in `test_trees.py`:
- `test_parse_price_valid` — asserts `"€79,500.00"` parses to `79500.0`
- `test_parse_price_invalid` — asserts a malformed string raises `ValueError`

See the "CSV parsing" and "Price parsing" entries in the Implementation Decisions section of the PRD for the exact interfaces.

## Acceptance criteria

- [ ] `load_properties(filepath)` returns a list of dicts with keys matching the CSV headers
- [ ] `load_properties` uses `utf-8-sig` encoding to handle a potential BOM
- [ ] `parse_price("€79,500.00")` returns `79500.0`
- [ ] `parse_price` raises `ValueError` naturally on malformed input (no custom exception wrapping)
- [ ] File I/O errors (`FileNotFoundError`, etc.) propagate without being caught or re-wrapped
- [ ] Both price tests pass with inline string data (no real files required)
- [ ] No runtime dependencies beyond stdlib

## Blocked by

None - can start immediately

## User stories addressed

- User story 7
- User story 10
- User story 11
- User story 12
- User story 13
