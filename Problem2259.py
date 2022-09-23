# Problem 2259: Remove Digit From Number to Maximize Result
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

input_number = 1232 # Number
digit = 2 # Digit

# Finding the number of occurrances of the digit in the
def finding_all_instances_of_digit(number, digit):
    global digit_count
    global number_list
    number_list = [int(x) for x in str(number)]
    digit_count = []
    digit_counter = -1

    # Getting the index value of each duplicate digit in the number
    for character in number_list:
        digit_counter += 1
        if character == digit:
            digit_count.append(digit_counter)

finding_all_instances_of_digit(input_number, digit)

# For a given index, it deletes the digit instance at the position and then saves that resulting value at maximum_result
def removing_digit_from_number(index):
    global maximum_result
    # Creating a list to store all of the values 
    maximum_result = []
    edited_number_list = number_list.copy()

    edited_number_list.pop(index)
    edited_number = int(''.join(map(str, edited_number_list)))
    maximum_result.append(edited_number)

for digit_instance in digit_count:
    removing_digit_from_number(digit_instance)

# Outputing the greatest result from removing_digit_from_number() 
print("The highest result of taking an instance of {} is {}.".format(digit, max(maximum_result)))
