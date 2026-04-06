"""
Module: palindrome_checker.py
Description: Determines if the provided text reads the same forwards and backwards.
Logic: Normalizes input (lowercase, no spaces) and compares the string to its slice-reversed version.
"""

def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

def main():
    try:
        n = input("ENTER THE STRING: ").strip()
        if not n:
            print("Input is empty.")
            return
            
        if is_palindrome(n):
            print("ENTERED STRING IS A PALINDROME")
        else:
            print("ENTERED STRING IS NOT A PALINDROME")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()