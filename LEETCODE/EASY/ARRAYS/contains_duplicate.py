"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.

Example 1:
    Input : nums = [1, 2, 3, 1]
    Output: True

Example 2:
    Input : nums = [1, 2, 3, 4]
    Output: False

Constraints:
    - 1 <= nums.length <= 10^5

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def contains_duplicate(nums):
    return len(nums) != len(set(nums))


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    print(f"CONTAINS DUPLICATE: {contains_duplicate(nums)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
