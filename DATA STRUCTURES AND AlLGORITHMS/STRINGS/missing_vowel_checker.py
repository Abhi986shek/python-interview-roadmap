"""
Prints all vowels missing from the input string.
"""
try:
    user_input = input("ENTER THE STRING\n")
    vowels = "AEIOUaeiou"
    for v in vowels:
        if v not in user_input:
            print(v)
except Exception as e:
    print(f"Error: {e}")