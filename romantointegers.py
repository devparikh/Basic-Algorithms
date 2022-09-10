import sys
# Creating a dictionary of key-value pairs to be used as a reference source in the function
roman_numeral_characters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Input roman numeral
roman_number_input = "F"

def romantointegers(roman_numeral_characters, roman_numeral):
    character_values = []
    for character in roman_numeral:
        # Checking if each character of the input is a part of the roman_numeral_characters dictionary
        if character in roman_numeral_characters:
            character_value = roman_numeral_characters[character]
            character_values.append(character_value)

        else:
            # Checking if the input value is actually has characters from the roman_numeral_character dictionary
            print("Input roman numeral not in range of 1 and 3999")
            sys.exit()

    # The general rule is that if the largest value of a roman numeral is the last character then all of the previous characters values have to be subtracted from the largest one to get the integer value
    if character_values[-1] == max(character_values):
        difference = sum(character_values) - max(character_values)
        number_value = max(character_values) - difference
        print("The integer value of {} in integers is {}".format(roman_numeral, number_value))
    # If the rule above does not hold true, then the sum of character_values defined in the loop above is the integer value
    else:
        print("The integer value of {} in integers is {}".format(roman_numeral, sum(character_values)))

romantointegers(roman_numeral_characters, roman_number_input)
