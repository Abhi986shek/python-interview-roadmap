"""
Module: string_to_integer.py
Description: Manually converts a numeric string to an integer without using int().
Logic: Iterates through characters, shifts values by base-10, and adds the current 
digit value via ASCII offsets (ord).
"""

def convert_to_int():
    try:
        n = input("ENTER THE STRING-NUMBER: ").strip()
        m = 0
        for char in n:
            if '0' <= char <= '9':
                m = m * 10 + (ord(char) - ord('0'))
            else:
                raise ValueError(f"Non-numeric character '{char}' found.")
        
        print(f"AFTER CONVERTING THE INTEGER NUMBER IS {m}")
    except ValueError as ve:
        print(f"VALUE ERROR: {ve}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    convert_to_int()