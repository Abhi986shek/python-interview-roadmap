"""
Module: vowel_replacer.py
Description: Replaces all vowels in a string with underscores if the vowel count exceeds 3.
Logic: Counts vowels using a set lookup. If count > 3, replaces every vowel with '_';
otherwise the original string is returned unchanged.
"""
try:
    user_input = input("ENTER THE STRING\n")
    vowels = set("AEIOUaeiou")
    
    count = sum(1 for char in user_input if char in vowels)
    
    if count > 3:
        result = "".join(['_' if char in vowels else char for char in user_input])
    else:
        result = user_input
        
    print("AFTER CONVERTING")
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
