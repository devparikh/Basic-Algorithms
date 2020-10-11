# This is a program that I am making to find out how many e's are in a given word

def find_letters():
    word_input = input("What word do you want to input:").lower()
    letter_input = input("What is the letter that you want to find: ").lower()

    letter_value = 0

    for i in word_input:
        if i == letter_input:
            letter_value += 1
    print(f"There is {letter_value} in the word {word_input}")
find_letters()