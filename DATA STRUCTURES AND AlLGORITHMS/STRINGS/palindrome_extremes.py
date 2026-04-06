"""
Finds the shortest and longest palindromic substrings (min length 3).
"""
def is_palindrome(s):
    return s == s[::-1]

try:
    s = input("ENTER THE STRING\n")
    palindromes = []

    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)

    if not palindromes:
        print("No palindromes of length 3 or more found.")
    else:
        lowest = min(palindromes, key=len)
        highest = max(palindromes, key=len)
        
        print(f"Lowest Palindrome: {lowest}")
        # Matching Java logic: if highest is long enough, trim the ends
        if len(highest) > 3:
            print(f"Highest Palindrome (Middle): {highest[1:-1]}")
        else:
            print(f"Highest Palindrome: {highest}")
except Exception as e:
    print(f"An error occurred: {e}")