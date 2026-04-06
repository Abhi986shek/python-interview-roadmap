"""
Counts the number of words in a string without using split() logic manually.
"""
try:
    user_input = input("ENTER THE STRING\n")
    # split() handles the logic of ignoring leading/trailing/multiple spaces
    count = len(user_input.split())
    print(f"THE TOTAL NUMBER OF WORDS ARE => {count}")
except Exception as e:
    print(f"Error: {e}")