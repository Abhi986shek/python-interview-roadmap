"""
Checks whether the entered character is a vowel or not.
Case-insensitive — works for both 'A' and 'a'.
"""
def vowel_detector():
    try:
        c = input("ENTER THE CHARACTER.. ")

        # Validate input
        if len(c) != 1:
            raise ValueError("Please enter exactly one character.")

        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            print("ENTERED CHARACTER IS VOWEL :)")
        else:
            print("ENTERED CHARACTER IS NOT A VOWEL :(")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    vowel_detector()