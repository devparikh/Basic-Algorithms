prime_sum_list = []
n = 2000000

# Sieve of Eratosthenes is the most efficient algorithm for finding prime numbers that is equal to or lower than a given input n which is the upperbound which in this case is 2,000,000
def SieveofEratosthenes(upperbound, prime_summation_list):
    # Creating a bolean list of True's, where the multiples of numbers in the set of numbers between 0 and n will be turned into False as they are non-prime
    prime_set = [True for i in range(n)]
    # Setting initial value of current_num to 2 because we want to ignore 0 and 1 when calculating multiples as 0 does not have any and every number has 1 as a multiple
    current_num = 2

    # If you want to calculate the square of current_number which is just the value of the correct location of the while loop at a given time in the number set, then it need to be lower than the upper_bound
    while (current_num * current_num <= upperbound):
        if prime_set[current_num] == True:
            # Looping all of the multiples of a certain number in the set and setting them to False prime_set
            for multiple in range(current_num * current_num, upperbound, current_num):
                prime_set[multiple] = False
        # updating the counter to the current epoch number of the while loop
        current_num += 1
    # iterating over our number set of interest that starts at 2 and ends at 2 million
    for prime_number in range(2, upperbound):
        # checking if a given value in prime_set is True(Prime) or False(Non-Prime)
        if prime_set[prime_number] == True:
            # we are adding a prime number to the summation list
            prime_summation_list.append(prime_number)


SieveofEratosthenes(n, prime_sum_list)

print("The sum of all prime numbers under 2 million is {}".format(sum(prime_sum_list))) # Finding the sum of all of the primes under 2 million
