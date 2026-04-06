"""
Finding the Missing and Repeating Elements

In an array of size n containing values from 1 to n,
one number is missing and one is repeated. Find both.

Example:
Array: [3, 1, 3] -> Repeating: 3, Missing: 2
"""

def find_missing_and_repeating(arr):
    n = len(arr)
    seen = set()
    repeating = -1

    for num in arr:
        if num in seen:
            repeating = num
        seen.add(num)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    # actual_sum = expected_sum - missing + repeating
    missing = expected_sum - actual_sum + repeating

    return repeating, missing


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated, values from 1 to n)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    repeating, missing = find_missing_and_repeating(arr)
    print(f"REPEATING ELEMENT: {repeating}")
    print(f"MISSING ELEMENT: {missing}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
