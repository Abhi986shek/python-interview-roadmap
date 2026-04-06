"""
Identifies and prints only the characters that appear exactly once in the string.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    counts = Counter(user_input)

    print("\nTHE UNIQUE CHARACTERS ARE=>")
    # Maintains original order of appearance
    unique_chars = [char for char in user_input if counts[char] == 1]
    print("".join(unique_chars))
except Exception as e:
    print(f"An error occurred: {e}")
