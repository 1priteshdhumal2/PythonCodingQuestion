def func(n):
    if n < 0:
        print("Invalid input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return func(n - 1) + func(n - 2)
    
print(func(10))

n = 10
num1 = 0
num2 = 1
nextNum = num2
cnt = 1

while cnt <= n:
    print(nextNum)
    cnt += 1
    num1, num2 = num2, nextNum  
    nextNum = num1 + num2
print()