"""
Module: anagram_tester.py
Description: Checks whether two input strings are anagrams of each other.
Logic: Normalizes both strings to lowercase and removes spaces, then compares
their sorted character lists. Equal sorted lists means they are anagrams.
"""
try:
    s1 = input("ENTER THE FIRST STRING\n").lower().replace(" ", "")
    s2 = input("ENTER THE SECOND STRING\n").lower().replace(" ", "")
    if sorted(s1) == sorted(s2):
        print("ENTERED STRINGS ARE ANAGRAMS")
    else:
        print("ENTERED STRINGS ARE NOT ANAGRAMS")
except Exception as e:
    print(f"Error: {e}")