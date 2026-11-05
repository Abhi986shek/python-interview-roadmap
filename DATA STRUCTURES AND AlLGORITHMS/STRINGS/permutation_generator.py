"""
Generates all possible permutations of a given string.
"""
# from itertools import permutations

# try:
#     s = input("ENTER THE STRING\n")
#     print("THE PERMUTATIONS ARE")
#     for p in set(permutations(s)):
#         print("".join(p))
# except Exception as e:
#     print(f"Error: {e}")


def permute(s, start):

    if start == len(s):
        print("".join(s))
        return

    for i in range(start, len(s)):

        s[start], s[i] = s[i], s[start]

        permute(s, start + 1)

        s[start], s[i] = s[i], s[start]


s = input("ENTER THE STRING: ")

permute(list(s), 0)
