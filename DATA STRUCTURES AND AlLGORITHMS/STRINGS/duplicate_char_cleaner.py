"""
Iterates through a string and removes duplicate characters using index checking.
"""
try:
    user_input = input("ENTER THE STRING\n")
    result = ""

    for char in user_input:
        if char not in result:
            result += char

    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
