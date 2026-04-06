"""
Module: character_printer.py
Description: Prints each character of the input string on a separate line.
Logic: Iterates directly over the string since Python strings are natively iterable,
printing one character per line.
"""
try:
    user_input = input("ENTER THE STRING\n")
    # Python strings are natively iterable, no explicit conversion needed
    for char in user_input:
        print(char)
except EOFError:
    print("Error: Input interrupted.")
