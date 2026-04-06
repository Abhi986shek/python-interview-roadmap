"""
Finds the LCM (Least Common Multiple) of two numbers.
Returns 0 if either input is 0.
"""
def lcm():
    try:
        a = input("ENTER THE FIRST NUMBER.. ")
        b = input("ENTER THE SECOND NUMBER.. ")

        # Validate input
        if not (a.lstrip('-').isdigit() and b.lstrip('-').isdigit()):
            raise ValueError("Inputs must be valid integers.")

        a = int(a)
        b = int(b)

        # Handle zero case
        if a == 0 or b == 0:
            print(f"THE LCM OF {a} AND {b} is -> 0")
            return

        n = max(abs(a), abs(b))

        while True:
            if n % a == 0 and n % b == 0:
                break
            n += abs(a)

        print(f"THE LCM OF {a} AND {b} is -> {n}")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    lcm()