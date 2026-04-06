"""
Subarray with Zero Sum

Check if any contiguous subarray has a sum of zero.
Uses prefix sum + hashmap — if the same prefix sum appears twice,
the subarray between those two indices sums to zero.

Example:
Array: [4, 2, -3, 1, 6] -> True  (subarray [2, -3, 1])
Array: [4, 2, 0, 1, 6]  -> True  (subarray [0])

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def has_zero_sum_subarray(arr):
    seen = set()
    seen.add(0)
    prefix = 0

    for num in arr:
        prefix += num
        if prefix in seen:
            return True
        seen.add(prefix)

    return False


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    if has_zero_sum_subarray(arr):
        print("YES, A SUBARRAY WITH ZERO SUM EXISTS")
    else:
        print("NO SUBARRAY WITH ZERO SUM FOUND")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
