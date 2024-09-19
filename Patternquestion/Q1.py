def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
        
n = int(input("Enter the number: "))
pattern1(n)

# *****
# *****
# *****
# *****
# *****