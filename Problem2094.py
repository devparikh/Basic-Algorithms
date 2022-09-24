# Problem 2094: Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/ 
import numpy as np

nums_array = np.array([2, 1, 3, 0])
nums_list = [int(num) for num in nums_array]
integer_list = []

# Iterating over every number from 1-9 for a, 0 is excluded to exclude ints with leading zeros
for a in range(1, 10):
    # The tens digit can be any number from 0-9
    for b in range(0, 10):
        # Even integers are need, best way to do that is to have even numbers in the ones digit
        for c in range(0, 9, 2):
            first_digit = a * 100
            second_digit = b * 10
            third_digit = c

            # Creating a list for each digit of the integer
            list_integer = [a, b, c]

            # Calculating the number of duplicates of a, b and c in integer and in nums_list
            list_integer_a_count = list_integer.count(a)
            nums_list_a_count = nums_list.count(a)

            list_integer_b_count = list_integer.count(b)
            nums_list_b_count = nums_list.count(b)

            list_integer_c_count = list_integer.count(c)
            nums_list_c_count = nums_list.count(c)

            # Adding the digit values to create the integer
            integer = first_digit + second_digit + third_digit
            # Checking if the number of duplicates in the integer and nums_list are the same
            # If that condition is true, then each digit in integer is a part of num_list
            if list_integer_a_count == nums_list_a_count and list_integer_b_count == nums_list_b_count and list_integer_c_count == nums_list_c_count:
                integer_list.append(integer)

# Converting to array
integer_array = np.array(integer_list)
# Printing the resulting output array of integers that met the conditions
print("A sorted array of the unique integers between 100-900 that fit all of the conditions are and whose elements come from the input array are {}.".format(integer_array))





