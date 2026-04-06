"""
Reverses a number by treating it as a string.
Handles negative numbers by preserving the sign.
"""
def reverse_number():
    try:
        n = input("ENTER THE NUMBER THAT YOU WANT TO REVERSE: ")

        # Validate input (allow negative numbers)
        if not n.lstrip('-').isdigit():
            raise ValueError("Input must be a valid integer.")

        sign = '-' if n.startswith('-') else ''
        n = n.lstrip('-')

        reversed_str = ""

        for digit in n:
            reversed_str = digit + reversed_str

        print("\n\n")  # to match your spacing style
        print(sign + reversed_str)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    reverse_number()