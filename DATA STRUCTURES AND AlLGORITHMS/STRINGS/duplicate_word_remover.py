"""
Removes duplicate words from a string while maintaining the original word order.
"""
try:
    user_input = input("ENTER THE STRING\n")
    words = user_input.split()
    seen = set()
    result = []

    for word in words:
        if word not in seen:
            result.append(word)
            seen.add(word)

    print("THE MODIFIED STRING IS =>")
    print(" ".join(result))
except Exception as e:
    print(f"An error occurred: {e}")
