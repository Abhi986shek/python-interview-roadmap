"""
Prints the sum of all numbers from 1 to n with the full expression.
Example: 4 -> 1 + 2 + 3 + 4 = 10
"""
def sum_of_numbers():
    try:
        n = input("ENTER THE NUMBER UPTO WHICH YOU WANT TO SEE THE SUM.. ")

        # Validate input
        if not n.isdigit():
            raise ValueError("Input must be a non-negative integer.")

        n = int(n)

        total = 0
        expression = ""

        print(f"SO THE SUM UPTO {n} IS ...")

        for i in range(1, n + 1):
            total += i
            expression += str(i)

            if i < n:
                expression += " + "

        print(expression + " = " + str(total))

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    sum_of_numbers()