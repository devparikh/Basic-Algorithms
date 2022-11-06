# LeetCode Problem 231: Power of Two
# https://leetcode.com/problems/power-of-two/


input_number = 512

# Iterative Strategy
def power_of_two_iterative(number):
    resultant_value = 0
    exponent_counter = 0
    is_power_two = False
    while resultant_value <= number:
        if number == 1:
            print("2^0 = 1")
            is_power_two = True
        else:
            exponent_counter += 1
            resultant_value = 2**exponent_counter
            if resultant_value == number:
                print("2^{} = {}".format(exponent_counter, resultant_value))
                is_power_two = True
    
    if is_power_two == False:
        print("The input number {} is not a power of 2".format(number))

power_of_two_iterative(input_number)


    
