## Parent PRD

`issues/prd.md`

## What to build

Implement `extract_street_names(node)` in `trees.py` — a recursive generator that walks the arbitrarily nested trees JSON structure and yields street name strings (leaf keys whose values are integers). Also implement `load_tree_categories(filepath)` to load the JSON file and return two sets: one for `short` streets and one for `tall` streets.

Write the corresponding unit test `test_extract_street_names` in `test_trees.py` using a small hand-crafted nested dict (no real files required).

See the "JSON parsing" entry in the Implementation Decisions section of the PRD for the exact interface.

## Acceptance criteria

- [ ] `extract_street_names(node)` correctly yields all leaf keys at any nesting depth
- [ ] Intermediate structural keys (non-leaf dicts) are not included in the output
- [ ] `load_tree_categories(filepath)` returns a tuple of two sets: `(short_streets, tall_streets)`
- [ ] `test_extract_street_names` passes with inline dict data and covers both shallow and deep nesting
- [ ] No runtime dependencies beyond stdlib

## Blocked by

None - can start immediately

## User stories addressed

- User story 5
- User story 6
- User story 11
- User story 12
- User story 13
