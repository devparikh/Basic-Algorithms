# Importing the math library to do operations
import math

# Using recursion and iterative algorithm will calculate the factorial of number n
    # Taking input
def getfactorial(x):
    factorial_input = int(input("What factorial do you want to calculate?:"))
    factorial = factorial_input
     # Calculating the factorial
    
    if factorial == 1:
        return 1
    else:
            
        calculatefactorial = math.factorial(factorial)  
        print(" The factorial is {}".format(calculatefactorial))
getfactorial('x')