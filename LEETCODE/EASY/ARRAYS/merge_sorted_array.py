"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing
    order, and two integers m and n, representing the number of elements in
    nums1 and nums2 respectively.
    Merge nums2 into nums1 as one sorted array in-place.
    nums1 has a length of m + n where the last n elements are 0 (placeholders).

Example 1:
    Input : nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1, 2, 2, 3, 5, 6]

Example 2:
    Input : nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]

Constraints:
    - nums1.length == m + n
    - Both arrays are sorted in non-decreasing order

Time Complexity  : O(m + n)
Space Complexity : O(1)
"""


def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


try:
    raw1 = input("ENTER NUMS1 ELEMENTS (space separated, without trailing zeros)\n")
    raw2 = input("ENTER NUMS2 ELEMENTS (space separated)\n")

    nums1 = list(map(int, raw1.split()))
    nums2 = list(map(int, raw2.split()))
    m, n = len(nums1), len(nums2)

    nums1 += [0] * n

    result = merge(nums1, m, nums2, n)
    print(f"MERGED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
