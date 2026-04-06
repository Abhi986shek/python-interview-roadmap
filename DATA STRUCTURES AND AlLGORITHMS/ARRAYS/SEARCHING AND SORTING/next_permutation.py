"""
Finding the Next Permutation

Rearranges the array into the next lexicographically greater permutation.
If no greater permutation exists, returns the smallest (sorted) order.

Example:
Input:  [1, 2, 3] -> Output: [1, 3, 2]
Input:  [3, 2, 1] -> Output: [1, 2, 3]
"""

def next_permutation(arr):
    n = len(arr)
    i = n - 2

    # find the first decreasing element from the right
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        # find the element just greater than arr[i] from the right
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    # reverse the suffix
    arr[i + 1:] = arr[i + 1:][::-1]
    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = next_permutation(arr)
    print(f"NEXT PERMUTATION: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
