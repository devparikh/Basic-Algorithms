# Project Euler Problem 4: https://projecteuler.net/problem=4
number_set = list(range(900, 1000))

def largest_palindrome_product(numbers_set):
  global reverse_product_list
  global product_list
  
  number_counter = -1
  product_list = []
  reverse_product_list = []

  for numbers in numbers_set:
    current_number = numbers_set[number_counter]

    for num in number_set:
      if num != current_number:
        product = current_number * num
        product_list.append(product)
              
        reversed_product = str(product)[::-1]
        reversed_product = int(reversed_product)
        reverse_product_list.append(reversed_product)

    number_counter += 1

largest_palindrome_product(number_set)

palindrome_list = []
product_counter = -1

for product in product_list:
  product_counter += 1
  if product_list[product_counter] == reverse_product_list[
  product_counter]:
    palindrome_list.append(product_list[product_counter])
    palindrome_list = list(dict.fromkeys(palindrome_list))
  
print("The Greatest Product of 2 3-Digit Numbers is {}".format(max(palindrome_list))) ---> 9number_set = list(range(900, 1000))

def largest_palindrome_product(numbers_set):
  global reverse_product_list
  global product_list
  
  number_counter = -1
  product_list = []
  reverse_product_list = []

  for numbers in numbers_set:
    current_number = numbers_set[number_counter]

    for num in number_set:
      if num != current_number:
        product = current_number * num
        product_list.append(product)
              
        reversed_product = str(product)[::-1]
        reversed_product = int(reversed_product)
        reverse_product_list.append(reversed_product)

    number_counter += 1

largest_palindrome_product(number_set)

palindrome_list = []
product_counter = -1
for product in product_list:
  product_counter += 1
  if product_list[product_counter] == reverse_product_list[
  product_counter]:
    palindrome_list.append(product_list[product_counter])
    palindrome_list = list(dict.fromkeys(palindrome_list))
  
print("The Greatest Product of 2 3-Digit Numbers is {}".format(max(palindrome_list))) # ---> 906609
