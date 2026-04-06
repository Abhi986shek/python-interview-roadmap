"""
Module: caesar_cipher_tool.py
Description: Encrypts and decrypts text using the Caesar cipher with a fixed shift of 2.
Logic: Shifts each alphabetic character by n positions within its case range using
modular arithmetic. Non-alphabetic characters are left unchanged.
"""
def shift_text(text, n):
    res = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            res += chr((ord(char) - base + n) % 26 + base)
        else:
            res += char
    return res

try:
    s = input("ENTER THE STRING\n")
    encoded = shift_text(s, 2)
    print(f"ENCODED TEXT: {encoded}")
    print(f"DECODED TEXT: {shift_text(encoded, -2)}")
except Exception as e:
    print(f"Error: {e}")