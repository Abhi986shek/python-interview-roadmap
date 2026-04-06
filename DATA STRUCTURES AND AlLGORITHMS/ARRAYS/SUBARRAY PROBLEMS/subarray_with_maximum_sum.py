"""
Subarray with Maximum Sum (Kadane's Algorithm)

Find the contiguous subarray with the largest sum and print the subarray too.

Example:
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Max Sum: 6, Subarray: [4, -1, 2, 1]
"""

def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if current_sum + arr[i] < arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, arr[start:end + 1]


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
