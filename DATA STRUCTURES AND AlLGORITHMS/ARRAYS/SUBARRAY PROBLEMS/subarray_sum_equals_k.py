"""
Subarray Sum Equals K

Count the number of contiguous subarrays whose sum equals k.

Example:
Array: [1, 1, 1], k = 2 -> Count: 2
"""

def subarray_sum_equals_k(arr, k):
    count = 0

    for i in range(len(arr)):
        total = 0

        for j in range(i, len(arr)):
            total += arr[j]

            if total == k:
                count += 1

    return count


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    k = int(input("ENTER THE TARGET SUM K\n"))

    result = subarray_sum_equals_k(arr, k)
    print(f"NUMBER OF SUBARRAYS WITH SUM {k}: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
