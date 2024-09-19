# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1

def pattern6(n):
    for i in range(n):
        for j in range(n, i, -1):
            print(n - j + 1, end="")
        print()



n = int(input("Enter the number: "))
pattern6(n)