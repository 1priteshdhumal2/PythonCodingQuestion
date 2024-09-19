word = "geeks quiz practice code"

s = word.split()[::-1]
l = []

for i in s:
    l.append(i)

print(" ".join(s))


# def is_palindrome(string):
#     reversed_string = string[::-1]
#     return string == reversed_string

# # Test the function
# word = "madam"
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

# s = "nitin"
# n = len(s)
# x = 0

# for i in range(n):
#     if s[i] != s[n - i - 1]:
#         x = 1

# if x == 1:
#     print(f"{s}Not a palindrome")
# else:
#     print(f"{s} Palindrome")