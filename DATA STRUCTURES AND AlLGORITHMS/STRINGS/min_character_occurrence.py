"""
Identifies the character with the lowest frequency in the given string.
"""
from collections import Counter

try:
    user_input = input("ENTER THE STRING\n")
    if not user_input:
        raise ValueError("String is empty.")

    counts = Counter(user_input)
    min_char = min(counts, key=counts.get)

    for char, count in counts.items():
        print(f"{char} count is ={count}")

    print(f"{min_char} IS THE LOWEST ONE OCCURING WITH A COUNT OF ={counts[min_char]}")
except Exception as e:
    print(f"An error occurred: {e}")
