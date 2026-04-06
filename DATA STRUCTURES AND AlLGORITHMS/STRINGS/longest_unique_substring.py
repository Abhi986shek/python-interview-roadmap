"""
Finds the length of the longest substring without repeating characters.
"""
def length_of_longest_substring(s):
    max_length = 0
    start = 0
    used_chars = {}
    
    for i, char in enumerate(s):
        # If char is in current window, move start
        if char in used_chars and used_chars[char] >= start:
            start = used_chars[char] + 1
        
        used_chars[char] = i
        max_length = max(max_length, i - start + 1)
        
    return max_length

try:
    s = input("ENTER THE STRING\n")
    if not s.strip():
        raise ValueError("Input cannot be empty.")
    print(f"Length of longest unique substring: {length_of_longest_substring(s)}")
except Exception as e:
    print(f"Error: {e}")