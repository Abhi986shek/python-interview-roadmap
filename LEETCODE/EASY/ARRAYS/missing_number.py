"""
Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
    Input : nums = [3, 0, 1]
    Output: 2

Example 2:
    Input : nums = [0, 1]
    Output: 2

Example 3:
    Input : nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Output: 8

Constraints:
    - n == nums.length
    - All numbers are distinct

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    print(f"MISSING NUMBER: {missing_number(nums)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
