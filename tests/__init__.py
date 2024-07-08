"""
Documentation for Test Function:

Function: `test_functions(functions)`
- Purpose: Runs and reports the results of a list of test functions.
- Parameters:
  - `functions`: A list of test functions to be executed.

Process:
1. Initializes counters for total, fail, and ok tests.
2. Iterates through the list of test functions.
3. For each function:
   - Tries to execute the function.
   - Prints the first line of the function's docstring.
   - Increments the ok counter and prints "OK" if the function passes.
   - Catches `AssertionError`, prints the error message, and increments the fail counter if the function fails.
4. Prints a summary of total tests, tests that passed (OK), and tests that failed (FAIL).
5. Returns a dictionary with the counts of total, ok, and fail tests.

Example Output:
- "Test function description: OK" for a passing test.
- "FAIL - <error message>" for a failing test.

Comments:
- The score calculation line is commented out and can be uncommented if needed to display the percentage of passed tests.
"""


def test_functions(functions):
    """Test all functions."""
    total = 0
    fail = 0
    ok = 0
    for func in functions:
        try:
            print(f"{func.__doc__.strip().split(chr(10))[0]}: ", end="")
            func()
            print("OK")
            ok += 1
        except AssertionError as e:
            print("\n\n# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #")
            print(f"FAIL - {e}")
            print("# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #\n")
            fail += 1
        total += 1
    print(f"Total tests: {total}, OK: {ok}, FAIL: {fail}")

    # print(f"Score: {ok/total*100:.2f}%")

    return {"total": total, "ok": ok, "fail": fail}
