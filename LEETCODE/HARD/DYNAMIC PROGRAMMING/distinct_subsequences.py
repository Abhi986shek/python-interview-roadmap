"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.
"""

def num_distinct(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    
    return dp[m][n]


try:
    s = input("ENTER STRING S\n")
    t = input("ENTER STRING T\n")
    print(f"DISTINCT SUBSEQUENCES: {num_distinct(s, t)}")
except Exception as e:
    print(f"An error occurred: {e}")
