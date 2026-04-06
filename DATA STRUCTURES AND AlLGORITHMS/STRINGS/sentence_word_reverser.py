"""
Module: sentence_word_reverser.py
Description: Reverses the sequence of words in a sentence.
Logic: Splits the string by whitespace, reverses the resulting list, 
and joins it back into a string.
"""

def reverse_sentence():
    try:
        n = input("ENTER THE STRING: ").strip()
        if not n:
            return
            
        words = n.split()
        reversed_sentence = " ".join(words[::-1])
        
        print(f"THE REVERSED STRING IS: {reversed_sentence}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    reverse_sentence()