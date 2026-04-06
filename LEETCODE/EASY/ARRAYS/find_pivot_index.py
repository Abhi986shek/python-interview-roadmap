"""
Find Pivot Index

Given an array of integers nums, calculate the pivot index.
The pivot index is the index where the sum of all numbers strictly to
the left equals the sum of all numbers strictly to the right.
Return the leftmost pivot index, or -1 if no such index exists.

Example 1:
    Input : nums = [1, 7, 3, 6, 5, 6]
    Output: 3

Example 2:
    Input : nums = [1, 2, 3]
    Output: -1

Example 3:
    Input : nums = [2, 1, -1]
    Output: 0

Constraints:
    - 1 <= nums.length <= 10^4

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, num in enumerate(nums):
        if left == total - left - num:
            return i
        left += num
    return -1


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    print(f"PIVOT INDEX: {pivot_index(nums)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
