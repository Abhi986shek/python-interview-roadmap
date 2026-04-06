"""
Search in Rotated Sorted Array

A sorted array is rotated at some pivot. Find the index of a target value.
Returns -1 if not found.

Example:
Array: [4, 5, 6, 7, 0, 1, 2], Target: 0 -> Index: 4
"""

def search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    target = int(input("ENTER THE TARGET VALUE\n"))

    result = search_rotated(arr, target)

    if result != -1:
        print(f"TARGET {target} FOUND AT INDEX {result}")
    else:
        print(f"TARGET {target} NOT FOUND IN THE ARRAY")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
