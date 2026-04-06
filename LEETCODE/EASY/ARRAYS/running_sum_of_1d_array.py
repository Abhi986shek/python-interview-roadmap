"""
Running Sum of 1D Array

Given an array nums, return the running sum where
runningSum[i] = sum(nums[0] + nums[1] + ... + nums[i]).

Example 1:
    Input : nums = [1, 2, 3, 4]
    Output: [1, 3, 6, 10]

Example 2:
    Input : nums = [1, 1, 1, 1, 1]
    Output: [1, 2, 3, 4, 5]

Constraints:
    - 1 <= nums.length <= 1000

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    print(f"RUNNING SUM: {running_sum(nums)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
