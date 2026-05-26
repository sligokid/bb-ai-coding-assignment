## Parent PRD

`issues/prd.md`

## What to build

Write `README.md` at the project root with the minimum instructions a developer needs to set up, run, and test the program. Package all source files into a single zip for submission.

The README must cover: Python version requirement, virtual environment setup, installing pytest, running the program with example CLI arguments, and running the test suite.

## Acceptance criteria

- [ ] `README.md` exists at the top level of the project
- [ ] README states the minimum Python version (3.10+)
- [ ] README includes setup instructions (`venv` creation and activation, `pip install pytest`)
- [ ] README includes a `run` example: `python main.py dublin-trees.json dublin-property.csv`
- [ ] README includes a `test` command: `pytest`
- [ ] Zip file contains exactly: `main.py`, `trees.py`, `test_trees.py`, `README.md`
- [ ] No compiled files, virtual environment directories, or data files are included in the zip

## Blocked by

- Blocked by `issues/001-parse-trees-json.md`
- Blocked by `issues/002-parse-property-csv.md`
- Blocked by `issues/003-compute-averages-and-cli.md`

## User stories addressed

- User story 14
- User story 15
- User story 16
