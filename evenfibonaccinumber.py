# Here I am creating the 3 most important variables to create the fibonacci sequence
number = [0,1]
fib_series = []
# Here I am having a while loop to make sure that the number n is less then 4000000
while n <= 4000000:
    n = before_previous_num + previous_num
    # Here its checking if n is even and if it is even then its adding the value to the list and printing the sum of that list
    if n % 2 == 0:
        fib_series += n
    print(sum(fib_series))
         


            

        
    
