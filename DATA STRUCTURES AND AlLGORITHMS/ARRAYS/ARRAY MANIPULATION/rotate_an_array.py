"""
Rotate an Array

Rotate the array to the right by k steps.

Example:
Array: [1, 2, 3, 4, 5, 6, 7], k = 3 -> [5, 6, 7, 1, 2, 3, 4]
"""

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # handle k greater than array length

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE NUMBER OF STEPS TO ROTATE\n"))

    if k < 0:
        raise ValueError("Steps cannot be negative.")

    result = rotate_array(arr, k)
    print(f"ARRAY AFTER ROTATING BY {k} STEPS: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
