"""
Module: compressed_string_expander.py
Description: Expands a compressed string where each letter is followed by a repeat count.
Example: "a3b2c1" expands to "aaabbc".
Logic: Uses regex to extract (letter, count) pairs and repeats each letter accordingly.
"""
import re

try:
    n = input("ENTER THE STRING\n")
    matches = re.findall(r'([a-zA-Z])(\d+)', n)
    result = "".join([char * int(num) for char, num in matches])
    print(f"THE OUT PUT IS=> {result}")
except Exception as e:
    print(f"Error: {e}")