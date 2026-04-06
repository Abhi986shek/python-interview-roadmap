"""
Module: case_toggler.py
Description: Swaps the case of every character in the input string.
Logic: Uses Python's built-in swapcase() method which converts all uppercase
letters to lowercase and all lowercase letters to uppercase in a single pass.
"""
try:
    user_input = input("ENTER THE STRING\n")
    # Built-in optimized method for case swapping
    print("AFTER CHANGING THE CASE")
    print(user_input.swapcase())
except Exception as e:
    print(f"An error occurred: {e}")
