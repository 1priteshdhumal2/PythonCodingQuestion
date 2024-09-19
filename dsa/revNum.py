n = int(input("Enter the number: "))
# 145

def reverseNum(n):
    revNum = 0

    while(n > 0):
        lastDigit = n % 10

        revNum = (revNum * 10) + lastDigit

        n = n // 10

    return revNum

print(reverseNum(n))