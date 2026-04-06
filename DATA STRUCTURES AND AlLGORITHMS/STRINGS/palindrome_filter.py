"""
Returns only the palindrome words from a given sentence.
"""
try:
    words = input("ENTER THE STRING\n").split()
    for word in words:
        if word.lower() == word[::-1].lower():
            print(word)
except Exception as e:
    print(f"Error: {e}")