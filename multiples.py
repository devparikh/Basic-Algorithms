# This is a simple algorithm that I made that is able to find multiples by on adding random nunbers with the input number

# importing libraries
import random

num_input = int(input("What is the number?"))

number = random.randint(1,1000)

multiples = []

new_number = num_input

while new_number < 100:
    new_number += number

    if new_number % num_input == 0:
        # This adds multiples to the multiples list
        multiples.append(new_number)
    else:
        continue
# This finds the sum of the multiples list
print(sum(multiples))
