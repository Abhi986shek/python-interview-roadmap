"""
Sort an Array of 0s, 1s and 2s (Dutch National Flag Problem)

Sort without using any sorting function — single pass.

Example:
Input:  [0, 1, 2, 1, 0, 2, 1]
Output: [0, 0, 1, 1, 1, 2, 2]
"""

def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (only 0s, 1s and 2s, space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    if any(x not in (0, 1, 2) for x in arr):
        raise ValueError("Array must contain only 0s, 1s and 2s.")

    result = sort_012(arr)
    print(f"SORTED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
