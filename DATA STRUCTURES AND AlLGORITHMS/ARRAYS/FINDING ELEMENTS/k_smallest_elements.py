"""
K Smallest Elements

Find and print the k smallest elements from the array in sorted order.

Example:
Array: [7, 10, 4, 3, 20, 15], k = 3 -> [3, 4, 7]
"""

def k_smallest_elements(arr, k):
    if k > len(arr):
        raise ValueError(f"k={k} is larger than array length {len(arr)}.")

    return sorted(arr)[:k]


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE VALUE OF K\n"))

    if k <= 0:
        raise ValueError("K must be greater than 0.")

    result = k_smallest_elements(arr, k)
    print(f"{k} SMALLEST ELEMENTS: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
