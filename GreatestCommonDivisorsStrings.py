# Initializing 2 random strings to be inputs of the function below
string_1 = "ABCABC"
string_2 = ""

# This function finds the greatest common divisors of 2 strings
def StringsGreatestCommonDivisors(string_input_1, string_input_2):
    greatest_common_divisors = []
    # Checking if both strings are empty
    if string_input_1 == "" and string_input_2 == "":
        print("Both of the input strings are invalid. Please Try Again.")

    # Checking if one of the strings is empty
    elif string_input_1 == "" or string_input_2 == "":
        print("One of the input strings are invalid. Please Try Again.")

    else:
        # Iterating over each element of both strings simultanously by zipping the 2 strings together, and the loop only iterates until the end of the shortest string
        for character_1, character_2 in zip(string_input_1, string_input_2):
            # Append the characters from each string to a list containing all of the characters of both strings
            greatest_common_divisors.append(character_1)
            greatest_common_divisors.append(character_2)

        # If the len of greatest_common_divisor is the same as the number of unique elements of the list, then that means that there are no duplicate characters or no common characters
        if len(greatest_common_divisors) == len(set(greatest_common_divisors)):
            print("No Greatest Common Divisor Found.")
        else:
            # If the condition above is false then the duplicate characters are removed from the greatest_common_divisors list through dict.fromkeys function
            greatest_common_divisor = list(dict.fromkeys(greatest_common_divisors))
            # Converting the list created from the function above to a string
            greatest_common_string = "".join(greatest_common_divisor)
            print("The Greatest Common String of string {} and {} is {}".format(string_input_1, string_input_2, greatest_common_string))
            
StringsGreatestCommonDivisors(string_1, string_2)