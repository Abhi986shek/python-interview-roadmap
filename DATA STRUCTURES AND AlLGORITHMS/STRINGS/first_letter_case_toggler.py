"""
Module: first_letter_case_toggler.py
Description: Toggles the case of the first letter of each word in a string.
If the first letter is lowercase it becomes uppercase, and vice versa.
Logic: Splits the string into words, applies swapcase() to the first character
of each word, and rejoins them.
"""
try:
    user_input = input("ENTER THE STRING\n")
    words = user_input.split(' ')
    result_list = []

    for word in words:
        if word:
            # Swap case of the first character and keep the rest
            transformed = word[0].swapcase() + word[1:]
            result_list.append(transformed)
        else:
            result_list.append("")

    print("AFTER USING IN IT CAP")
    print(" ".join(result_list))
except Exception as e:
    print(f"An error occurred: {e}")
