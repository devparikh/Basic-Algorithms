def getfactorial(x):
    factorial_input = int(input("What factorial do you want to calculate?:"))
    factorial = 1 
     # Calculating the factorial
    if factorial_input <= 1:
      print("This is not valid!")
    elif factorial_input > 0:
      for i in range(1, factorial_input+1):
        factorial= factorial * i 
      print("The factorial of {n} is {f}".format(n=factorial_input, f=factorial))
getfactorial('x')
  
