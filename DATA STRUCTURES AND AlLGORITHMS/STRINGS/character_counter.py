"""
Module: character_counter.py
Description: Counts the total number of characters in a user-provided string.
Logic: Iterates through each character using a for loop and increments a counter,
mimicking Java's Scanner useDelimiter("") character-by-character reading approach.
"""
try:
    s = input("ENTER THE STRING\n")
    if not s.strip():
        raise ValueError("Input cannot be empty.")
    count = 0
    for _ in s:
        count += 1
    print(count)
except Exception as e:
    print(f"Error: {e}")