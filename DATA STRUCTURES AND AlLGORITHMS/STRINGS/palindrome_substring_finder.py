"""
Finds and prints all substrings (length >= 3) that are palindromes.
"""
try:
    s = input("ENTER THE STRING\n")
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub.lower() == sub[::-1].lower():
                print(sub)
except Exception as e:
    print(f"Error: {e}")