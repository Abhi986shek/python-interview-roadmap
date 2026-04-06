"""
Move Zeroes

Given an integer array nums, move all 0s to the end of it while maintaining
the relative order of the non-zero elements.
You must do this in-place without making a copy of the array.

Example 1:
    Input : nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Example 2:
    Input : nums = [0]
    Output: [0]

Constraints:
    - 1 <= nums.length <= 10^4

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def move_zeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    while pos < len(nums):
        nums[pos] = 0
        pos += 1


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    move_zeroes(nums)
    print(f"ARRAY AFTER MOVING ZEROES: {nums}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
