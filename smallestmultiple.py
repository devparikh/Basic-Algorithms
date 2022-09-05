# Project Euler Problem 5: https://projecteuler.net/problem=5
# Starting at 2520 because thats the smallest multiple of the numbers between 1-10, so surely the smallest multiple of 1-20 will be greater than that
smallest_multiple_counter = 2520
# The upperbound of the factors is 20 and would be used to check if each of these divisors are divisible by the smallest_multiple_counter
factor_upperbound = 20

def smallest_multiple(counter, upperbound):
    for factor in range(1, upperbound+1):
        if counter % factor == 0:
            continue
        else:
            return False
    return True

while smallest_multiple(smallest_multiple_counter, factor_upperbound) == False:
    # Skipping by 20 because the next number must be divisible by 20 and thats why even if smallest_multiple_counter is divisible by all the numbers under 20, if its not divisible by 20 then it doesn't count
    smallest_multiple_counter += 20 

print("The smallest number that is divisible by the numbers between 1-20 is {}".format(smallest_multiple_counter))
# The smallest number that is divisible by the numbers between 1-20 is 232792560