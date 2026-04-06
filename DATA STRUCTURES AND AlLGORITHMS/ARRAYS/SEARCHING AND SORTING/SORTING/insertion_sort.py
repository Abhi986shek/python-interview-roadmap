"""
Insertion Sort

Builds the sorted array one element at a time.
Picks each element and inserts it into its correct position
among the already sorted elements to its left.

Time Complexity:
    Best    : O(n)   - already sorted
    Average : O(n²)
    Worst   : O(n²)  - reverse sorted

Space Complexity: O(1) - in-place sorting
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # shift elements greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = insertion_sort(arr)
    print(f"SORTED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
