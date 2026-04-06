"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""

def first_missing_positive(nums):
    n = len(nums)
    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1


try:
    nums = list(map(int, input("ENTER NUMBERS (space separated)\n").split()))
    print(f"FIRST MISSING POSITIVE: {first_missing_positive(nums)}")
except Exception as e:
    print(f"An error occurred: {e}")
