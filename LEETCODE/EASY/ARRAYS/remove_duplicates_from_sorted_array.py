"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same.
    Return k — the number of unique elements.

Example 1:
    Input : nums = [1, 1, 2]
    Output: 2, nums = [1, 2, _]

Example 2:
    Input : nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - Array is sorted in non-decreasing order

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def remove_duplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


try:
    raw = input("ENTER SORTED ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    k = remove_duplicates(nums)
    print(f"NUMBER OF UNIQUE ELEMENTS: {k}")
    print(f"ARRAY AFTER REMOVAL: {nums[:k]}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
