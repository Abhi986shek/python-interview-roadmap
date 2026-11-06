"""
Subarray with Maximum Sum (Kadane's Algorithm)

Find the contiguous subarray with the largest sum and print the subarray too.

Example:
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Max Sum: 6, Subarray: [4, -1, 2, 1]
"""

def max_subarray_sum(arr):
    max_sum = arr[0]
    best_subarray = []

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum += arr[j]

            if current_sum == max(current_sum, max_sum):
                if current_sum > max_sum:
                    best_subarray = arr[i:j + 1]

            max_sum = max(max_sum, current_sum)

    return max_sum, best_subarray


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    max_sum, subarray = max_subarray_sum(arr)
    print(f"MAXIMUM SUM: {max_sum}")
    print(f"SUBARRAY: {subarray}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
