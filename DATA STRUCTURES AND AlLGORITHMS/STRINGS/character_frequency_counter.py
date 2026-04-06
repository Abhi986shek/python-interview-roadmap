"""
Module: character_frequency_counter.py
Description: Prints the frequency of each character in the order they first appear.
Logic: Uses Counter to build a frequency map, then iterates the original string
with a seen set to print each character's count exactly once on first encounter.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    counts = Counter(user_input)
    seen = set()
    
    for char in user_input:
        if char not in seen:
            print(f"{char} count is ={counts[char]}")
            seen.add(char)
except Exception as e:
    print(f"An error occurred: {e}")
