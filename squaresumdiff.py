# Project Euler Problem 6: https://projecteuler.net/problem=6
upperbound = 100

sum_of_squares = []
square_of_sum = []

for num in range(1, upperbound+1):
    square_of_sum.append(num)
    num_square = num * num
    sum_of_squares.append(num_square)


squares_sum = sum(square_of_sum) * sum(square_of_sum)
sum_squares = sum(sum_of_squares)

difference = squares_sum - sum_squares

print("The difference between the sum of squares of the first {} natural numbers and it's square of the sum is {}".format(upperbound, difference))

# The difference between the sum of squares of the first 100 natural numbers and it's square of the sum is 25164150