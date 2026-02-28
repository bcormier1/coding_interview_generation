# Interview Practice

A Python project for practicing leetcode/hackerrank-style coding questions with pytest.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
uv sync --dev
```

## Project Structure

```
Questions/       # Problem statements and function stubs (write your code here)
Answers/         # Working solutions (answer key)
Tests/           # Pytest test files
```

Each problem uses the same filename across all three directories (e.g., `two_sum.py`).

## Included Questions

| Problem | Category |
|---------|----------|
| Two Sum | General |
| Group Anagrams | General |
| LRU Cache | General |
| Moving Average | Data Science |
| Find Outliers (IQR) | Data Science |

## Workflow

1. Open a question file in `Questions/` and read the problem statement
2. Write your solution in that file
3. Update the test file's import to point at your solution:
   ```python
   from Questions.two_sum import two_sum
   # from Answers.two_sum import two_sum
   ```
4. Run the tests:
   ```bash
   uv run pytest Tests/test_two_sum.py -v
   ```
5. Check the answer in `Answers/` if you get stuck

Run all tests at once with:

```bash
uv run pytest Tests/ -v
```

## Adding New Questions

Each problem uses the same snake_case filename across all three directories.

1. **`Questions/<name>.py`** -- Docstring with the problem statement, then function stub(s) with `pass` as the body. Include type hints.
2. **`Answers/<name>.py`** -- Working solution with the same function signature(s).
3. **`Tests/test_<name>.py`** -- At least 3 test cases. Default the import to the Answers module with the Questions import commented out:
   ```python
   # from Questions.<name> import <func>
   from Answers.<name> import <func>
   ```
4. Verify: `uv run pytest Tests/test_<name>.py -v`

## Using with Claude Code

This repo is designed to work with [Claude Code](https://docs.anthropic.com/en/docs/claude-code). You can use it to generate new problems and get feedback on your solutions.

### Generating new questions

```
Add a medium difficulty question about binary search trees
```

```
Add 3 easy string manipulation questions
```

```
Add a data science question involving normalization, similar in style to find_outliers
```

Be specific about the topic, difficulty, and category to get the best results. Claude will create all three files (question stub, answer, tests) and verify the tests pass.

### Getting feedback on your solution

After writing your solution in a `Questions/` file, ask Claude to review it:

```
Review my solution in Questions/two_sum.py. Run the tests and tell me what's
wrong if they fail. Don't show me the answer.
```

```
Look at my solution in Questions/find_outliers.py. How does my time complexity
compare to the answer key? What could I improve?
```

```
I'm stuck on Questions/lru_cache.py. Give me a hint about the right data
structure to use without giving away the full solution.
```

Key phrases to use:
- **"Don't show me the answer"** -- prevents Claude from spoiling the solution
- **"Give me a hint"** -- gets a nudge in the right direction without the full solution
- **"Compare to the answer key"** -- gets a complexity/style comparison after you've finished
