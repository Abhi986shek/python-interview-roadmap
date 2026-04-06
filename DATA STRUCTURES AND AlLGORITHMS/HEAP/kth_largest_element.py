"""
Kth Largest Element Using Min Heap

Maintain a min heap of size k. For each element, if it's larger than
the heap's minimum, replace it. The root of the heap is the kth largest.

Example:
Array: [3, 2, 1, 5, 6, 4], k = 2 -> 2nd Largest: 5

Time Complexity  : O(n log k)
Space Complexity : O(k)
"""

import heapq


def kth_largest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE VALUE OF K\n"))

    if k <= 0 or k > len(arr):
        raise ValueError(f"K must be between 1 and {len(arr)}.")

    result = kth_largest(arr, k)
    print(f"{k}TH LARGEST ELEMENT: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
