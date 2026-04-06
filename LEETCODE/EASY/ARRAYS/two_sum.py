"""
Two Sum

Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input : nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Example 2:
    Input : nums = [3, 2, 4], target = 6
    Output: [1, 2]

Constraints:
    - 2 <= nums.length <= 10^4
    - Each input has exactly one solution

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))
    target = int(input("ENTER TARGET\n"))

    result = two_sum(nums, target)
    print(f"INDICES: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
