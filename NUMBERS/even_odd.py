"""
Checks whether a number is even, odd, or zero.
Works with decimal inputs too.
"""
def even_odd():
    try:
        n = input("ENTER THE NUMBER.. ")

        # Validate input
        n = float(n)

        if n == 0:
            print("ENTERED NUMBER IS 'ZERO'")
        elif n % 2 == 0:
            print("ENTERED NUMBER IS AN 'EVEN NUMBER'")
        else:
            print("ENTERED NUMBER IS AN 'ODD NUMBER'")

    except ValueError:
        print("Error: Please enter a valid number.")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    even_odd()