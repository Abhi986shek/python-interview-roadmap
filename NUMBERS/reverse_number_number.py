"""
Reverses a number using integer arithmetic.
Handles negative numbers by preserving the sign.
"""
def reverse_number():
    try:
        n = input("ENTER THE NUMBER: ")

        # Validate input (allow negative numbers)
        if not n.lstrip('-').isdigit():
            raise ValueError("Input must be a valid integer.")

        n = int(n)

        sign = -1 if n < 0 else 1
        n = abs(n)

        reversed_num = 0

        while n > 0:
            reversed_num = (reversed_num * 10) + (n % 10)
            n //= 10

        reversed_num *= sign

        print("THE REVERSED NUMBER IS ->", reversed_num)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    reverse_number()