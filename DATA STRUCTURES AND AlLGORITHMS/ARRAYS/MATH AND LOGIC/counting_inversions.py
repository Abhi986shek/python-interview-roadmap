"""
Counting the Inversions

Count the number of pairs (i, j) where i < j but arr[i] > arr[j].
Uses merge sort for O(n log n) time.

Example:
Array: [2, 4, 1, 3, 5] -> Inversions: 3 (pairs: (2,1), (4,1), (4,3))
"""

def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_count(arr[:mid])
    right, right_inv = merge_count(arr[mid:])

    merged = []
    inversions = left_inv + right_inv
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # all remaining elements in left are greater than right[j]
            inversions += len(left) - i
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    _, count = merge_count(arr)
    print(f"NUMBER OF INVERSIONS: {count}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
