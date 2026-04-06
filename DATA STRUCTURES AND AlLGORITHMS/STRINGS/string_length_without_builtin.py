"""
Module: string_length_without_builtin.py
Description: Calculates the length of a string without using the built-in len() function.
Logic: Iterates through each character using a for loop and increments a counter manually.
"""
try:
    sc = input("ENTER THE STRING\n")
    count = 0
    # Iterating through the string to count characters
    for char in sc:
        count += 1
    
    print(f"THE LENGTH IS {count}")
except EOFError:
    print("Error: Input interrupted.")