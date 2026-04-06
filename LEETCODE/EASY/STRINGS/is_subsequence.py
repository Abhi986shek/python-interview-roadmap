"""
Is Subsequence

Given two strings s and t, return true if s is a subsequence of t,
or false otherwise.
A subsequence is a string that can be derived from another string by
deleting some characters without changing the relative order of the remaining characters.

Example 1:
    Input : s = "abc", t = "ahbgdc"
    Output: True

Example 2:
    Input : s = "axc", t = "ahbgdc"
    Output: False

Constraints:
    - 0 <= s.length <= 100
    - 0 <= t.length <= 10^4

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def is_subsequence(s, t):
    i = 0
    for c in t:
        if i < len(s) and c == s[i]:
            i += 1
    return i == len(s)


try:
    s = input("ENTER STRING S\n")
    t = input("ENTER STRING T\n")

    print(f"IS SUBSEQUENCE: {is_subsequence(s, t)}")

except Exception as e:
    print(f"An error occurred: {e}")
