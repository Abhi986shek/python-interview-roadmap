"""
Binary to Decimal Conversion.
Validates that input only contains 0s and 1s before converting.
"""
def binary_to_decimal():
    try:
        bin_num = int(input("ENTER THE BINARY NUMBER: "))

        i = 1
        deci = 0
        n = bin_num

        while n > 0:
            digit = n % 10

            # Validate binary digit (must be 0 or 1)
            if digit not in (0, 1):
                raise ValueError("Invalid binary number! Only 0 and 1 are allowed.")

            deci = deci + digit * i
            i *= 2
            n //= 10

        print("DECIMAL CONVERSION OF", bin_num, "IS ->", deci)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    binary_to_decimal()