"""
Subarray Sum Equals K

Count the number of contiguous subarrays whose sum equals k.

Example:
Array: [1, 1, 1], k = 2 -> Count: 2
"""

def subarray_sum_equals_k(arr, k):
    count = 0
    prefix_sum = 0
    # stores how many times a prefix sum has occurred
    freq = {0: 1}

    for num in arr:
        prefix_sum += num

        # if (prefix_sum - k) was seen before, those subarrays sum to k
        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

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
