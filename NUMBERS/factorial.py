"""
Calculates the factorial of a number and prints the full expression.
Example: 5 -> 1 x 2 x 3 x 4 x 5 = 120
"""
def factorial():
    try:
        n = input("ENTER THE NUMBER: ")

        # Validate input
        if not n.isdigit():
            raise ValueError("Input must be a non-negative integer.")

        n = int(n)

        fact = 1
        expression = ""

        for i in range(1, n + 1):
            fact *= i
            expression += str(i)
            if i < n:
                expression += " x "

        print("SO THE FACTORIAL OF THE NUMBER IS --")
        print(expression + " = " + str(fact))

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    factorial()