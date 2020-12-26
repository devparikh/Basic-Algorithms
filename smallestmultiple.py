import random

num_input = int(input("What is the number?"))

number = random.randint(1,10)

multiples = []

new_number = num_input

while new_number < 100:
    new_number += number

    if new_number % num_input == 0:
        multiples.append(new_number)
    else:
        continue
print(sum(multiples))
        
