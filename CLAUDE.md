# Code Quality
Always run `ruff format` after making code changes

# Adding New Questions

Each problem uses the same snake_case filename across all three directories.

1. **`Questions/<name>.py`** — Docstring with the problem statement (title, description, constraints, examples). Below it, define the function stub(s) with `pass` as the body. Include type hints on parameters and return type.

2. **`Answers/<name>.py`** — Working solution with the same function signature(s). No docstring needed.

3. **`Tests/test_<name>.py`** — Pytest test file. Include at minimum 3 test cases covering basic, edge, and non-trivial inputs. The import should default to the Answers module with the Questions import commented out above it:
   ```python
   # from Questions.<name> import <func>
   from Answers.<name> import <func>
   ```

Run `uv run pytest Tests/test_<name>.py` to verify all tests pass against the answer.

# Reviewing User Solutions

When asked to review a solution in `Questions/`:

- Run the tests first (`uv run pytest Tests/test_<name>.py -v`) and report pass/fail results.
- If the user says "don't show me the answer" or "no spoilers", do NOT read or reference code from `Answers/`. Only use test output to guide feedback.
- If the user asks for a "hint", give a conceptual nudge (e.g., "consider using a hash map") without showing implementation details or reading the answer file.
- If the user asks to "compare to the answer key", read both files and discuss differences in time/space complexity, readability, and edge case handling.
- Point out any issues: bugs, inefficiencies, missing edge cases, or style problems. Be direct.
