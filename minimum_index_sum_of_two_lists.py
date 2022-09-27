list_1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list_2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

# Using a dictionary for easy identification of a given key(string) and its corresponding value or its indexes sum value
common_string_index = dict()
def find_minimum_index_sum_lists(list_1, list_2, common_strings):
    # Iterating over every string in list_1 and checking if its present in list_2
    for string_1 in list_1:
        if string_1 in list_2:
            # Taking the index of this string in list 1 and 2
            list_1_index = list_1.index(string_1)
            list_2_index = list_2.index(string_1)
            # Finding the index sum by taking the sum of the index of the string in both lists
            least_index_sum = list_1_index + list_2_index
            common_string_index[string_1] = least_index_sum

find_minimum_index_sum_lists(list_1, list_2, common_string_index)

# Iterate with over each value in the dictionary
for value in common_string_index.values():
    # if the value is the lowest of all of the values in the dictionary, then do the following.
    if value == min(common_string_index.values()):
        # iterating over every key where the item(value of a given key-value pair) == to value(variable created above)
        keys = [key for key, item in common_string_index.items() if item == value]
        common_string = keys

# Print the resulting output string with the least index sum
print("The common string with the least index sum is {}.".format(common_string))