"""
Finding the Missing Number from 1 to N

Given an array of n-1 integers from 1 to n with one missing, find it.

Example:
Array: [1, 2, 4, 5, 6], n = 6 -> Missing: 3
"""

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    n = int(input("ENTER THE VALUE OF N (total numbers from 1 to N)\n"))

    if n <= 0:
        raise ValueError("N must be greater than 0.")

    if len(arr) != n - 1:
        raise ValueError(f"Array should have exactly {n - 1} elements for range 1 to {n}.")

    result = find_missing_number(arr, n)
    print(f"MISSING NUMBER: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
