"""
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:
    Input : nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    Output: [2]

Example 2:
    Input : nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
    Output: [9, 4]

Constraints:
    - 1 <= nums1.length, nums2.length <= 1000

Time Complexity  : O(n + m)
Space Complexity : O(n)
"""


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


try:
    raw1 = input("ENTER FIRST ARRAY (space separated)\n")
    raw2 = input("ENTER SECOND ARRAY (space separated)\n")

    nums1 = list(map(int, raw1.split()))
    nums2 = list(map(int, raw2.split()))

    if not nums1 or not nums2:
        raise ValueError("Both arrays must have at least one element.")

    print(f"INTERSECTION: {intersection(nums1, nums2)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
