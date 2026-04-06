"""
Maximum Subarray Sum of Contiguous Elements

Given an array and a window size k, find the maximum sum of any
contiguous subarray of exactly k elements.

Example:
Array: [2, 1, 5, 1, 3, 2], k = 3 -> Max Sum: 9 (subarray [5, 1, 3])
"""

def max_sum_of_k_elements(arr, k):
    n = len(arr)

    if k > n:
        raise ValueError(f"Window size {k} is larger than array length {n}.")

    # sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE WINDOW SIZE K\n"))

    if k <= 0:
        raise ValueError("Window size must be greater than 0.")

    result = max_sum_of_k_elements(arr, k)
    print(f"MAXIMUM SUM OF {k} CONTIGUOUS ELEMENTS: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
