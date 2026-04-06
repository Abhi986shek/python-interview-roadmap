"""
Checks if the input string contains every letter of the English alphabet at least once.
"""
import string

def is_pangram(text):
    # Set of all lowercase letters
    alphabet = set(string.ascii_lowercase)
    # Set of lowercase letters in the input string
    input_letters = set(text.lower())
    # Check if alphabet is a subset of input
    return alphabet.issubset(input_letters)

try:
    user_input = input("ENTER THE STRING\n")
    if is_pangram(user_input):
        print("ENTERED STRING IS PANGRAM")
    else:
        print("ENTERED STRING IS NOT PANGRAM")
except Exception as e:
    print(f"An error occurred: {e}")
