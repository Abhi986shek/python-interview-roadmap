"""
Removes redundant consecutive spaces from a string, 
ensuring only a single space remains between words.
"""
try:
    user_input = input("ENTER THE STRING\n")
    # split() without arguments handles any amount of whitespace
    result = " ".join(user_input.split())
    
    print("AFTER REMOVING DUPLICATE SPACES")
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
