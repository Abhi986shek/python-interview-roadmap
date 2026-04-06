"""
Adds digits of a number repeatedly until a single digit remains.
Example: 493 -> 4+9+3=16 -> 1+6=7
"""
def adding_digits():
    try:
        num = input("ENTER THE NUMBER: ")

        # Validate input
        if not num.isdigit():
            raise ValueError("Input must be a non-negative integer.")

        total = int(num)

        while total > 9:
            n = total
            total = 0

            while n > 0:
                total += n % 10
                n //= 10

            print(total)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    adding_digits()