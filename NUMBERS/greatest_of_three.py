"""
Finds the greatest among three numbers.
Accepts decimal values too.
"""
def greatest_of_three():
    try:
        a = input("ENTER THE FIRST NUMBER.. ")
        b = input("ENTER THE SECOND NUMBER.. ")
        c = input("ENTER THE THIRD NUMBER.. ")

        # Validate input
        a = float(a)
        b = float(b)
        c = float(c)

        if a > b and a > c:
            print(f"{a} IS THE GREATEST OF THE 3.")
        elif b > c:
            print(f"{b} IS THE GREATEST OF THE 3.")
        else:
            print(f"{c} IS THE GREATEST OF THE 3.")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    greatest_of_three()