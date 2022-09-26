# Problem 2273: Find Resultant Array after Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

import numpy as np
anagram_array = np.array(["abba","baba","bbaa","cd","cd"])

# Function that finds all of the anagrams in an array
def finding_anagrams_from_array(input_array):
    global sorted_word_list
    sorted_word_list = []
    string_index = -1
    # Iterating over each element and sorting each string so we can see the sets of anagrams and other string

    for word in range(0, len(input_array)):
        string_index += 1
        word = input_array[string_index]

        word = sorted(word)
        word = "".join(word)
        sorted_word_list.append(word)

finding_anagrams_from_array(anagram_array)

# Creating an empty list for the output strings
# Unique_elements which is a dictionary that will contain all of the unique strings of the input array
output_list = []
# Dictionaries are used because they are containers that have unique keys and unique values
unique_elements = dict()
index = -1

# Iterating over each element in the sorted list of the input array
for word in sorted_word_list:
    index += 1
    # Checking if a word is unique and if it then adding it to the dictionary
    if word not in unique_elements:
        unique_elements[word] = 0
        # since this is a unique element, we will add it to output array
        output_list.append(anagram_array[index])

output_array = np.array(output_list)
print("The resultant array after removing anagrams is {}.".format(output_array))

