"""
Move All Zeros to the End

Move all 0s to the end while maintaining the relative order of non-zero elements.

Example:
Array: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
"""

def move_zeros_to_end(arr):
    pos = 0  # position to place the next non-zero element

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    while pos < len(arr):
        arr[pos] = 0
        pos += 1

    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = move_zeros_to_end(arr)
    print(f"ARRAY AFTER MOVING ZEROS TO END: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
