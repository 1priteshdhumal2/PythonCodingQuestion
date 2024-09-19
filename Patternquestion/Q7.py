# Result:
#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********

def pattern7(n):
    for i in range(n):
        for j in range(0, n - i - 1):
            print(" ", end="")
        for k in range(0, 2*i+1):
            print("*", end="")
        for j in range(0, n - i):
            print(" ", end="")
        print()

n = int(input("Enter the number: "))
pattern7(n)