"""
Finding the Peak Element

A peak element is greater than its neighbors.
Returns the index of any one peak element using binary search.

Example:
Array: [1, 2, 3, 1] -> Peak Index: 2 (value 3)
"""

def find_peak_element(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    idx = find_peak_element(arr)
    print(f"PEAK ELEMENT: {arr[idx]} AT INDEX {idx}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
