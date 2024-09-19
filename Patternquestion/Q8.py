# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

def pattern8(n):
    for i in range(n):
        for j in range(0, i):
            print(" ", end="")
        for j in range(0, (2 * n) - (2 * i + 1)):
            print("*", end="")
        print()


n = int(input("Enter the number: "))
pattern8(n)