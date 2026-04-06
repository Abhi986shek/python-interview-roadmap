"""
Module: vowel_detector.py
Description: Counts the total number of vowels present in a given string.
Logic: Uses a set of vowel characters for O(1) lookup efficiency and a 
generator expression to sum occurrences of 'A, E, I, O, U'.
"""

def count_vowels():
    try:
        s = input("ENTER THE STRING: ")
        vowels = set("AEIOUaeiou")
        count = sum(1 for char in s if char in vowels)
        
        print(f"THE NUMBER OF VOWELS IN THE ENTERED STRING IS {count}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    count_vowels()