"""
Module: string_variable_swapper.py
Description: Swaps the values of two string variables without using a temporary variable.
Logic: Concatenates both strings into the first variable, then extracts the original
values back using string slicing based on their lengths.
"""
try:
    a = input("ENTER THE VALUE OF A\n")
    b = input("ENTER THE VALUE OF B\n")
    
    a = a + b
    b = a[:len(a) - len(b)]
    a = a[len(b):]
    
    print(f"AFTER SWAPPING\nA = {a}\nB = {b}")
except Exception as e:
    print(f"Error: {e}")