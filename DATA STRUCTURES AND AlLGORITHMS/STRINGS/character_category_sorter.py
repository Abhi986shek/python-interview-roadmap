"""
Module: character_category_sorter.py
Description: Rearranges all characters in a string by category: digits first, then
special characters, then lowercase letters, then uppercase letters.
Logic: Groups characters into four separate lists by type and joins them in order.
"""

def arrange_string():
    try:
        s = input("ENTER THE STRING: ")
        num, spec, lc, uc = [], [], [], []
        
        for char in s:
            if char.isdigit(): num.append(char)
            elif char.islower(): lc.append(char)
            elif char.isupper(): uc.append(char)
            else: spec.append(char)
            
        result = "".join(num + spec + lc + uc)
        print("\nTHE STRING IN ARRANGED ORDER IS...")
        print(result)
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    arrange_string()