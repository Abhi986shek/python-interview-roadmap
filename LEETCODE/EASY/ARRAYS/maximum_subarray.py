"""
Maximum Subarray

Given an integer array nums, find the subarray with the largest sum
    and return its sum.

Example 1:
    Input : nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: Subarray [4, -1, 2, 1] has the largest sum = 6.

Example 2:
    Input : nums = [1]
    Output: 1

Example 3:
    Input : nums = [5, 4, -1, 7, 8]
    Output: 23

Constraints:
    - 1 <= nums.length <= 10^5

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def max_subarray(nums):
    max_sum = nums[0]
    current = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)

    return max_sum


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    print(f"MAXIMUM SUBARRAY SUM: {max_subarray(nums)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
