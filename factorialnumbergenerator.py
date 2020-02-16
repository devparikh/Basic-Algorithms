
def getfactorial(x):
    factorial_input = int(input("What factorial do you want to calculate?:"))
    factorial = factorial_input
     # Calculating the factorial
    
    if factorial == 1:
        return 1
    else:
            
        for x in range(1, factorial):
            factorial = factorial * x
            return factorial  
        print(" The factorial is {}".format(calculatefactorial))
getfactorial('x')