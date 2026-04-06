"""
Bubble Sort

Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
The largest element "bubbles up" to its correct position after each pass.

Time Complexity:
    Best    : O(n)      - already sorted (with early exit)
    Average : O(n²)
    Worst   : O(n²)

Space Complexity: O(1) - in-place sorting
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # no swaps means array is already sorted
        if not swapped:
            break

    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = bubble_sort(arr)
    print(f"SORTED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
