"""
Sliding Window Maximum

Find the maximum element in every window of size k as it slides across the array.
Uses a deque to keep track of useful indices in O(n) time.

Example:
Array: [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]

Time Complexity  : O(n)
Space Complexity : O(k)
"""

from collections import deque


def sliding_window_max(arr, k):
    n = len(arr)
    result = []
    dq = deque()  # stores indices, front always holds the max of current window

    for i in range(n):
        # remove indices outside the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # remove indices whose values are smaller than current element
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # start recording results once the first window is complete
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE WINDOW SIZE K\n"))

    if k <= 0 or k > len(arr):
        raise ValueError(f"K must be between 1 and {len(arr)}.")

    result = sliding_window_max(arr, k)
    print(f"MAXIMUMS IN EACH WINDOW OF SIZE {k}: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
