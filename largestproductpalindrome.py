# Project Euler Problem 4: https://projecteuler.net/problem=4
palindrome_list = []
three_digit_numbers = []

def largest_palindrome_product(numbers_set, palindrome_list):
  number_counter = 0
  product_list = []
  for number in range(900, 999):
    numbers_set.append(number)

    current_number = numbers_set[number_counter]

    for num in numbers_set:
      if num != current_number:
        product = current_number * num
        product_list.append(product)

    reverse_product_list = str(product_list)[::-1]

    if product_list == reverse_product_list:
      palindrome_list.append(product_list[0:len(product_list)])

    number_counter += 1


largest_palindrome_product(three_digit_numbers, palindrome_list)
 
print(max(palindrome_list)) # in three digits products the largest palindrome product is 906609 which is the product of 913 and 993
