"""
Kth Largest Element

Find the kth largest element in an unsorted array.

Example:
Array: [3, 2, 1, 5, 6, 4], k = 2 -> 2nd Largest: 5
"""

def kth_largest(arr, k):
    if k > len(arr):
        raise ValueError(f"k={k} is larger than array length {len(arr)}.")

    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[k - 1]


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE VALUE OF K\n"))

    if k <= 0:
        raise ValueError("K must be greater than 0.")

    result = kth_largest(arr, k)
    print(f"{k}TH LARGEST ELEMENT: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
