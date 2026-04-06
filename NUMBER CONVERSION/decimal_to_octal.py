"""
Decimal to Octal Conversion
"""
def decimal_to_octal():
    try:
        dec = input("ENTER THE DECIMAL NUMBER: ")

        if not dec.isdigit():
            raise ValueError("Input must be a valid non-negative integer.")

        dec = int(dec)

        octal = 0
        i = 1

        while dec > 0:
            a = dec % 8
            octal = a * i + octal
            i = i * 10
            dec //= 8

        print("THE OCTAL NUMBER IS ->", octal)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    decimal_to_octal()