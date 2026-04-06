"""
Sum of Array Elements in a Given Range

Find the sum of all elements between index l and r (inclusive).

Example:
Array: [1, 2, 3, 4, 5], l = 1, r = 3 -> Sum: 9 (2 + 3 + 4)
"""

def range_sum(arr, l, r):
    return sum(arr[l:r + 1])


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    l = int(input("ENTER THE LEFT INDEX\n"))
    r = int(input("ENTER THE RIGHT INDEX\n"))

    if l < 0 or r >= len(arr) or l > r:
        raise ValueError(f"Invalid range. Valid indices are 0 to {len(arr) - 1} and l must be <= r.")

    print(f"SUM OF ELEMENTS FROM INDEX {l} TO {r}: {range_sum(arr, l, r)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
