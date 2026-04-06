"""
Octal to Decimal Conversion.
Validates that all digits are in range 0-7 before converting.
"""
def octal_to_decimal():
    try:
        oct_num = input("ENTER THE OCTAL NUMBER: ")

        # Validate input is numeric
        if not oct_num.isdigit():
            raise ValueError("Input must be a valid number.")

        oct_num = int(oct_num)

        i = 1
        deci = 0
        n = oct_num

        while n > 0:
            digit = n % 10

            # Validate octal digit (0–7)
            if digit > 7:
                raise ValueError("Invalid octal number! Digits must be between 0 and 7.")

            deci += digit * i
            i *= 8
            n //= 10

        print("DECIMAL CONVERSION OF", oct_num, "IS ->", deci)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    octal_to_decimal()