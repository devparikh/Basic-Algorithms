# Here I am creating the 3 most important variables to create the fibonacci sequence
before_previous_num = 1
previous_num = 1
n = 0
fib_series = 0
# Here I am having a while loop to make sure that the number n is less then 4000000
while n < 4000000:
    n = before_previous_num + previous_num
    # Here its checking if n is even and if it is even then its adding the value to the list and printing the sum of that list
    if n % 2 == 0:
        fib_series += n
        
    # Here we are changing the values to make sure that they are changing every time the loop starts again 
    previous_num = before_previous_num
    n = previous_num
print(fib_series)
         


            

        
    