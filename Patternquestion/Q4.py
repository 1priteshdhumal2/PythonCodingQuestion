# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

def pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()

n = int(input("Enter the number: "))
pattern4(n)