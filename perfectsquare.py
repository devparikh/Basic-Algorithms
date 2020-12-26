# This is a simple algorithm I made that is able to take an input and add random numbers and check if it is a perfect square

# importing libraries
import random

num_input = int(input("What is the number?"))

number = random.randint(1,1000)

perfect_squares = []

new_number = num_input

while new_number > 10000:
    new_number += number

    perfect_square = new_number ** 0.5

    if perfect_square == int:
        perfect_squares.append(perfect_square)
    else:
        continue
print(sum(perfect_squares))