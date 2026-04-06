"""
Heap Sort

Builds a max-heap from the array, then repeatedly extracts the maximum
element and places it at the end. Uses the heap property to sort in-place.

Time Complexity:
    Best    : O(n log n)
    Average : O(n log n)
    Worst   : O(n log n)

Space Complexity: O(1) - in-place sorting
"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build max-heap from the bottom up
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = heap_sort(arr)
    print(f"SORTED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
