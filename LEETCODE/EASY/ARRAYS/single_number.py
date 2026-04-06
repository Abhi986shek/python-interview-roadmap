"""
Single Number

Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.
You must implement a solution with linear runtime complexity and
use only constant extra space.

Example 1:
    Input : nums = [2, 2, 1]
    Output: 1

Example 2:
    Input : nums = [4, 1, 2, 1, 2]
    Output: 4

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - Every element appears twice except for one

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out pairs
    return result


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    print(f"SINGLE NUMBER: {single_number(nums)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
