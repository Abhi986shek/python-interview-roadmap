"""
Finds the longest common prefix among an array of strings.
"""
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Sorting ensures we only need to compare the first and last strings
    strs.sort()
    first = strs[0]
    last = strs[-1]
    
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]

try:
    raw = input("ENTER STRINGS SEPARATED BY COMMAS\n")
    if not raw.strip():
        raise ValueError("Input cannot be empty.")
    strs = [s.strip() for s in raw.split(",")]
    print(f"Longest Common Prefix: {longest_common_prefix(strs)}")
except Exception as e:
    print(f"Error: {e}")