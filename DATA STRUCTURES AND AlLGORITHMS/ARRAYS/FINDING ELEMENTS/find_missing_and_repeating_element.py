"""
Finding the Missing and Repeating Elements

In an array of size n containing values from 1 to n,
one number is missing and one is repeated. Find both.

Example:
Array: [3, 1, 3] -> Repeating: 3, Missing: 2
"""

def find_missing_and_repeating(arr):
    seen = set()
    repeating = set()

    for num in arr:
        if num in seen:
            repeating.add(num)
        seen.add(num)

    expected_sum = len(arr) * (len(arr) + 1) // 2
    actual_sum = sum(arr)

    missing = expected_sum - actual_sum + sum(repeating)

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
