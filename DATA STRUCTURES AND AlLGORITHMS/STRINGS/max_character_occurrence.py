"""
Identifies the character with the highest frequency in the given string.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    if not user_input:
        raise ValueError("String is empty.")

    counts = Counter(user_input)
    max_char = max(counts, key=counts.get)

    for char, count in counts.items():
        print(f"{char} count is ={count}")

    print(f"{max_char} IS THE HIGHEST ONE OCCURING WITH A COUNT OF ={counts[max_char]}")
except Exception as e:
    print(f"An error occurred: {e}")
