"""
Decimal to Binary Conversion — result stored as a string.
Example: 5 -> "101"
"""
def decimal_to_binary():
    try:
        dec = input("ENTER THE DECIMAL NUMBER: ")

        # Validate input
        if not dec.isdigit():
            raise ValueError("Input must be a valid non-negative integer.")

        dec = int(dec)

        binary = ""

        # Special case for 0
        if dec == 0:
            binary = "0"

        while dec > 0:
            a = dec % 2
            binary = str(a) + binary
            dec //= 2

        print("THE BINARY NUMBER IS ->", binary)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    decimal_to_binary()