palindrome_input = input("What is your number that you want to find the palindrome of?")

if palindrome_input == palindrome_input.backward():
    print("{} is a palindrome".format(palindrome_input))
else:
    print("This is not a palindrome")