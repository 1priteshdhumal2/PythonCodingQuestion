#Brute force approach
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = int(input("enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not prime number")

# 2.optimal approch
import math

def checkPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
        
    return True

print(checkPrime(int(input("Enter a number: "))))


def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
    
for i in range(100, 0, -1):
    if isPrime(i):
        print(i, end=" ")