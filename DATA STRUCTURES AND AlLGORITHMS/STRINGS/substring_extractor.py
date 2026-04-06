"""
Prints all possible substrings in a word (minimum length 3).
"""
try:
    s = input("ENTER THE STRING\n")
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            print(s[i:j])
except Exception as e:
    print(f"Error: {e}")