"""
Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than n/2 times.
You may assume that the majority element always exists in the array.

Example 1:
    Input : nums = [3, 2, 3]
    Output: 3

Example 2:
    Input : nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Constraints:
    - n == nums.length
    - 1 <= n <= 5 * 10^4
    - The majority element always exists

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def majority_element(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


try:
    raw = input("ENTER ARRAY ELEMENTS (space separated)\n")
    nums = list(map(int, raw.split()))

    if not nums:
        raise ValueError("Array cannot be empty.")

    print(f"MAJORITY ELEMENT: {majority_element(nums)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
