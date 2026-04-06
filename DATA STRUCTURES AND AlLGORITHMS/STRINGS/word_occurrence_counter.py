"""
Checks and prints the occurrence frequency of each word in a string.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    words = user_input.split()
    counts = Counter(words)
    
    for word, count in counts.items():
        print(f"{word} count is = {count}")
except Exception as e:
    print(f"Error: {e}")