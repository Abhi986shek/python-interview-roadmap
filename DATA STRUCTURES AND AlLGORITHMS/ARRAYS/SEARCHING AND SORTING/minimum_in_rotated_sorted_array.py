"""
Minimum in Rotated Sorted Array

A sorted array is rotated at some pivot. Find the minimum element.

Example:
Array: [3, 4, 5, 1, 2] -> Minimum: 1
"""

def find_minimum(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # mid is greater than right means min is in right half
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    print(f"MINIMUM ELEMENT IN THE ROTATED ARRAY IS {find_minimum(arr)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
