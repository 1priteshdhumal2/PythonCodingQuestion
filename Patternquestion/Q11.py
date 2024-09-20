# 1
# 2 3
# 4 5 6

def pattern11(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=" ")
            num += 1
        print()

pattern11(5)