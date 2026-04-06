"""
Module: extract_alphabets.py
Description: Filters out all non-alphabetic characters from a string.
Logic: Uses the .isalpha() method to identify letters and joins them into a single string.
"""

def extract_alphabets():
    try:
        s = input("ENTER THE STRING: ")
        result = "".join(char for char in s if char.isalpha())
        
        print(f"THE EXTRACTED ALPHABETS FROM ENTERED STRING IS {result}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    extract_alphabets()