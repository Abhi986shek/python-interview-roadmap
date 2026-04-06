"""
Selection Sort

Divides the array into a sorted and unsorted region.
In each pass, finds the minimum element from the unsorted region
and places it at the beginning of that region.

Time Complexity:
    Best    : O(n²)
    Average : O(n²)
    Worst   : O(n²)

Space Complexity: O(1) - in-place sorting
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # swap only if a smaller element was found
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = selection_sort(arr)
    print(f"SORTED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
