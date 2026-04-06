"""
Module: word_characters_reverser.py
Description: Reverses the characters within each individual word while keeping word order intact.
Logic: Splits the sentence into words, reverses each word's characters using slicing [::-1],
and joins them back with spaces.
"""

def reverse_individual_words():
    try:
        n = input("ENTER THE STRING: ").strip()
        if not n:
            return
            
        words = [word[::-1] for word in n.split()]
        result = " ".join(words)
        
        print(f"THE REVERSED STRING IS: {result}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    reverse_individual_words()