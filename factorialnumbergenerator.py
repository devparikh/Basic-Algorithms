# Importing the math library to do operations
import math

# Using recursion and iterative algorithm will calculate the factorial of number n
def getfactorial(n):
    # Taking input
    factorial_input = int(input("What factoial do you want to calculate?:"))
    factorial = factorial_input
    
     # Calculating the factorial
    for x in range(1, factorial):
        if factorial == '1':
            return '1'
        else:
            x * math.factorial(x - 1)

getfactorial(n)

         

        


