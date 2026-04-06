"""
Module: string_reverser.py
Description: Reverses the entire input string using Python's slicing method [::-1].
Logic: Reads a string from the user and prints the character-by-character reverse.
"""

def reverse_string():
    try:
        user_input = input("ENTER THE NUMBER/STRING: ").strip()
        if not user_input:
            raise ValueError("Input cannot be empty.")
            
        reversed_str = user_input[::-1]
        print(f"THE REVERSE OF ENTERED INPUT IS {reversed_str}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    reverse_string()