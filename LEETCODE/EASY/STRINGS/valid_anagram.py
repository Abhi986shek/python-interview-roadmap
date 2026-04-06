"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
An anagram is a word formed by rearranging the letters of another word.

Example 1:
    Input : s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input : s = "rat", t = "car"
    Output: False

Constraints:
    - 1 <= s.length, t.length <= 5 * 10^4
    - s and t consist of lowercase English letters

Time Complexity  : O(n)
Space Complexity : O(1)  - at most 26 unique characters
"""

from collections import Counter


def is_anagram(s, t):
    return Counter(s) == Counter(t)


try:
    s = input("ENTER FIRST STRING\n")
    t = input("ENTER SECOND STRING\n")

    print(f"IS ANAGRAM: {is_anagram(s, t)}")

except Exception as e:
    print(f"An error occurred: {e}")
