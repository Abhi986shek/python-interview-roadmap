"""
Generates all possible permutations of a given string.
"""
from itertools import permutations

try:
    s = input("ENTER THE STRING\n")
    print("THE PERMUTATIONS ARE")
    for p in set(permutations(s)):
        print("".join(p))
except Exception as e:
    print(f"Error: {e}")