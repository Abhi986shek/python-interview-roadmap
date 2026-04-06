"""
Quick Sort

A divide and conquer algorithm. Picks a pivot element and partitions
the array so all elements smaller than the pivot go left and all
greater go right. Recursively sorts both partitions.

Time Complexity:
    Best    : O(n log n)
    Average : O(n log n)
    Worst   : O(n²)     - when pivot is always the smallest or largest element

Space Complexity: O(log n) - recursive call stack
"""

def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    quick_sort(arr, 0, len(arr) - 1)
    print(f"SORTED ARRAY: {arr}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
