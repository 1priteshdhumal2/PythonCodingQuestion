    #  *
    #  **
    #  *** 
    #  ****
    #  *****
    #  ******  
    #  *****
    #  ****
    #  ***    
    #  **
    #  *

def pattern10(n):
    for i in range(1, 2 * n):
        stars = i
        if(i > n):
            stars = 2 * n - i
        for j in range(1,stars + 1):
            print("*", end="")
        print()

pattern10(6)