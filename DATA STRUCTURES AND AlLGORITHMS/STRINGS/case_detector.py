"""
Module: case_detector.py
Description: Analyzes a string to count Uppercase, Lowercase, Numeric, and Special characters.
Logic: Iterates through each character and uses built-in string methods (.isupper, .isdigit, etc.) 
to categorize and increment respective counters.
"""

def detect_cases():
    try:
        s = input("ENTER THE STRING: ")
        uc, lc, nc, sc = 0, 0, 0, 0
        
        for char in s:
            if char.isupper():
                uc += 1
            elif char.islower():
                lc += 1
            elif char.isdigit():
                nc += 1
            else:
                sc += 1
                
        print(f"THE NUMBER OF UPPERCASE LETTERS: {uc}")
        print(f"THE NUMBER OF LOWERCASE LETTERS: {lc}")
        print(f"THE NUMBER OF DIGITS: {nc}")
        print(f"THE NUMBER OF SPECIAL CHARACTERS: {sc}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    detect_cases()