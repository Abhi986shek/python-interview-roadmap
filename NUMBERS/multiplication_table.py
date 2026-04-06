"""
Prints the multiplication table (1 to 10) for a given number.
"""
def multiplication_table():
    try:
        n = input("ENTER THE NUMBER, FOR WHICH YOU WANT THE MULTIPLICATION TABLE: ")

        # Validate input
        if not n.isdigit():
            raise ValueError("Input must be a valid non-negative integer.")

        n = int(n)

        print(f"SO THE MULTIPLICATION TABLE FOR {n} is .....")

        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    multiplication_table()