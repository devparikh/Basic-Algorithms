import math
# By applying the conditions for special pythagorean triplet and checking the range for each of the numbers a and b, these are the upperbounds for both variables
a_upperbound = 250
b_upperbound = 380

found = False

a = 1
b = 1

# Checking if the triplet is found, if false then continue else break
while found == False:
    # Iterating over every number in range from 1 to the variable b upperbound 
    for b in range(1, b_upperbound):
        b += 1
        # Iterating over every number in range from 1 to the variable a upperbound 
        for a in range(1, a_upperbound):
            a += 1 

            # Finding the value of c by adding the squares of a and b and then finding its square root
            squared_a = a * a
            squared_b = b * b
            c = math.sqrt(squared_a + squared_b)
            squared_c = c * c

            condition = a + b + c
            product = a * b * c
            # Ensuring that a is smaller than b and b is smaller than c and that condition which is the sum of the 3 variables is 1000
            if a < b < c and condition == 1000:
                # Printing the triplet if found
                print("The special pythagorean triplet with A: {}, B: {} and C: {} whose sum is 1000 is {}".format(a, b, c, product))
                found = True



"""
for number in range(1, len(specialpythagoreantriplet)):
    random.shuffle(specialpythagoreantriplet)
    c = random.choice(specialpythagoreantriplet)
    b = random.choice(specialpythagoreantriplet)
    a = random.choice(specialpythagoreantriplet)

    abc_combo.append(a)
    abc_combo.append(b)
    abc_combo.append(c)

    all_combo.append(abc_combo)

    squared_a = a * a
    squared_b = b * b
    squared_c = c * c 

    nums_sum = a + b + c

    if a < b < c and squared_a + squared_b == squared_c and nums_sum == 1000:
        print("The special pythagorean triplet whose sum is 1000 is {}".format(nums_sum))
"""