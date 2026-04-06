"""
Kth Smallest Element Using Max Heap

Maintain a max heap of size k. For each element, if it's smaller than
the heap's maximum, replace it. The root of the heap is the kth smallest.

Example:
Array: [7, 10, 4, 3, 20, 15], k = 3 -> 3rd Smallest: 7

Time Complexity  : O(n log k)
Space Complexity : O(k)
"""

import heapq


def kth_smallest(arr, k):
    # Python only has min heap, negate values to simulate max heap
    max_heap = []

    for num in arr:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return -max_heap[0]


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE VALUE OF K\n"))

    if k <= 0 or k > len(arr):
        raise ValueError(f"K must be between 1 and {len(arr)}.")

    result = kth_smallest(arr, k)
    print(f"{k}TH SMALLEST ELEMENT: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
