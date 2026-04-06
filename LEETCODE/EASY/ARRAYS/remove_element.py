"""
Remove Element

Given an integer array nums and an integer val, remove all occurrences
    of val in-place. The order of the elements may be changed.
    Return k — the number of elements not equal to val.

Example 1:
    Input : nums = [3, 2, 2, 3], val = 3
    Output: 2, nums = [2, 2, _, _]

Example 2:
    Input : nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
    Output: 5, nums = [0, 1, 3, 0, 4, _, _, _]

Constraints:
    - 0 <= nums.length <= 100

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))
    val = int(input("ENTER VALUE TO REMOVE\n"))

    k = remove_element(nums, val)
    print(f"COUNT AFTER REMOVAL: {k}")
    print(f"ARRAY: {nums[:k]}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
