"""
Module: character_frequency_by_replacement.py
Description: Counts the frequency of each character by repeatedly removing it from the string.
Logic: Takes the first character, removes all its occurrences using replace(), calculates
the count from the length difference, then repeats for the next remaining character.
"""
try:
    s1 = input("ENTER THE STRING\n")
    while s1:
        char = s1[0]
        s2 = s1.replace(char, "")
        print(f"{char} = {len(s1) - len(s2)}")
        s1 = s2
except Exception as e:
    print(f"Error: {e}")