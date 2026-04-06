"""
Smallest Missing Positive Number

Find the smallest positive integer that is not present in the array.

Example:
Array: [3, 4, -1, 1] -> Answer: 2
Array: [1, 2, 3]     -> Answer: 4
"""

def smallest_missing_positive(arr):
    n = len(arr)

    # place each number in its correct index position (num at index num-1)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    print(f"SMALLEST MISSING POSITIVE NUMBER: {smallest_missing_positive(arr)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
