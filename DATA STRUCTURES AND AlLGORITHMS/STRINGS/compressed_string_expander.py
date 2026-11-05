"""
Module: compressed_string_expander.py
Description: Expands a compressed string where each letter is followed by a repeat count.
Example: "a3b2c1" expands to "aaabbc".
Logic: Uses regex to extract (letter, count) pairs and repeats each letter accordingly.
"""
try:
    n = input("ENTER THE STRING\n")
    result = ""
    char = ""

    for i in n:
        if i.isalpha():
            char = i
        elif i.isdigit():
            result += char * int(i)

    print(f"THE OUTPUT IS => {result}")

except Exception as e:
    print(f"Error: {e}")
