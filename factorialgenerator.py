def getfactorial():
    factorial_input = int(input("What factorial do you want to calculate?:"))
    factorial = 1 
     # Calculating the factorial
    if factorial_input == 1:
      print("The value is 1")
    elif factorial_input > 0:
      for i in range(1, factorial_input+1):
        factorial= factorial * i 
      print("The factorial of {n} is {f}".format(n=factorial_input, f=factorial))
    if factorial_input == 0:
        print("The factorial of 0 is 1!")
    elif factorial_input < 0:
        print("Invalid Input! Please try another factorial")
        factorial_input()
        
        
getfactorial()
  
