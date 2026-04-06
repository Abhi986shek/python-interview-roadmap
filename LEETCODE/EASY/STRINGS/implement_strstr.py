"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters.
"""


def str_str(haystack, needle):
    if not needle:
        return 0
    return haystack.find(needle)


try:
    haystack = input("ENTER HAYSTACK\n")
    needle = input("ENTER NEEDLE\n")
    result = str_str(haystack, needle)
    print(f"INDEX: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
