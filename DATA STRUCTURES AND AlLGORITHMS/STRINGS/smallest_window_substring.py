"""
Finds the smallest window in s1 containing all characters of s2.
"""
from collections import Counter

def find_smallest_window(s1, s2):
    if not s2 or not s1: return ""
    
    target_count = Counter(s2)
    required = len(target_count)
    
    l, r = 0, 0
    formed = 0
    window_counts = {}
    
    # (length, left, right)
    ans = float("inf"), None, None
    
    while r < len(s1):
        char = s1[r]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_count and window_counts[char] == target_count[char]:
            formed += 1
            
        while l <= r and formed == required:
            char = s1[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            
            window_counts[char] -= 1
            if char in target_count and window_counts[char] < target_count[char]:
                formed -= 1
            l += 1
        r += 1
        
    return "" if ans[0] == float("inf") else s1[ans[1] : ans[2] + 1]

try:
    s1 = input("ENTER THE MAIN STRING\n")
    s2 = input("ENTER THE PATTERN STRING\n")
    if not s1.strip() or not s2.strip():
        raise ValueError("Both inputs cannot be empty.")
    result = find_smallest_window(s1, s2)
    print(f"Smallest window: {result if result else 'No window found'}")
except Exception as e:
    print(f"Error: {e}")