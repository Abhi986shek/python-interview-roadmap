"""
Marks consecutive duplicate characters by inserting a '$' symbol between them.
Example: "aabb" -> "a$ab$b"
"""
try:
    user_input = input("ENTER THE STRING\n")

    if not user_input:
        print("")
    else:
        result = [user_input[0]]

        for i in range(1, len(user_input)):
            if user_input[i] == user_input[i - 1]:
                result.append('$')

            result.append(user_input[i])

        print("AFTER CONVERTING")
        print("".join(result))

except Exception as e:
    print(f"An error occurred: {e}")
