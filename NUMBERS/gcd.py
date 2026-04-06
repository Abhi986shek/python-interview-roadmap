"""
Finds the GCD (Greatest Common Divisor) of two numbers.
Handles negatives and zero inputs.
"""
def gcd():
    try:
        a = input("ENTER THE FIRST NUMBER.. ")
        b = input("ENTER THE SECOND NUMBER.. ")

        # Validate input
        if not (a.lstrip('-').isdigit() and b.lstrip('-').isdigit()):
            raise ValueError("Inputs must be valid integers.")

        a = int(a)
        b = int(b)

        # Handle zero cases
        if a == 0 and b == 0:
            raise ValueError("GCD is undefined for both numbers zero.")

        n = min(abs(a), abs(b))

        while True:
            if a % n == 0 and b % n == 0:
                break
            n -= 1

        print(f"THE GCD OF {a} AND {b} is -> {n}")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    gcd()