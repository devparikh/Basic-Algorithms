# Here I am creating the 3 most important variables to create the fibonacci sequence
number = [0,1]
fib_series = []
# Here I am having a while loop to make sure that the number n is less then 4000000
for i in range(1,4000000):
  fib_sequence = number[i] + number[i+1]
    # Here its checking if n is even and if it is even then its adding the value to the list and printing the sum of that list
  if i % 2 == 0:
    fib_series += i
  print(sum(fib_series))


            

        
    
