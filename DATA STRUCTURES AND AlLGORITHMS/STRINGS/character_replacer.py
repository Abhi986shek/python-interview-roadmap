"""
Module: character_replacer.py
Description: Replaces all occurrences of the letter 'a' with the '@' symbol in a string.
Logic: Uses Python's built-in str.replace() method for direct character substitution.
"""
try:
    user_input = input("ENTER THE STRING\n")
    print(user_input.replace('a', '@'))
except Exception as e:
    print(f"Error: {e}")