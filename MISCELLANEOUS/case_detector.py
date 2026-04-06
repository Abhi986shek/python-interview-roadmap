"""
Checks whether the entered character is lowercase, uppercase, a digit, or a special character.
"""
def case_detector():
    try:
        c = input("ENTER THE CHARACTER.. ")

        # Validate input
        if len(c) != 1:
            raise ValueError("Please enter exactly one character.")

        if 'a' <= c <= 'z':
            print("ENTERED CHARACTER IS LOWERCASE")
        elif 'A' <= c <= 'Z':
            print("ENTERED CHARACTER IS UPPERCASE")
        elif '0' <= c <= '9':
            print("ENTERED CHARACTER IS A NUMBER")
        else:
            print("ENTERED CHARACTER IS A SPECIAL CHARACTER")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    case_detector()