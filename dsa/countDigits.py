def countDigits(n):
    ans = []

    while n > 0:
        lastDigit = n % 10
        ans.append(lastDigit)
        n = n // 10

    # ans.reverse()
    return ans

# print(countDigits(2479852))

def countDigits1(n):
    cnt = 0

    while n > 0:
        cnt += 1
        n = n // 10

    return cnt

print(countDigits1(25753))
