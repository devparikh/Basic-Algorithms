sorted_list_1 = [10, 10, 12, 15, 17, 19]
sorted_list_2 = [12, 15, 19, 17, 21, 30]
# Merging sorted lists
combo_list = sorted_list_1 + sorted_list_2

# Creating a function to sort the merged list
def sort_merged_lists(combo_list):
    # Iterating over every number in the merged list
    for number in range(len(combo_list)):
        # Since the bubble sort algorithm checks the next number in the sequence we want to cap that until the second last value or else the program will crash 
        for num in range(len(combo_list) - 1):
            # We are checking the number next to num or num + 1 instead of num - 1 because the algorithm would crash for the first number in merged_list as it does not have a previous value
            if combo_list[num] > combo_list[num + 1]:
                # Saving the value of the current position as position_1
                position_1 = combo_list[num]

                # Changing changing current value num to num + 1
                combo_list[num] = combo_list[num + 1]

                # Doing the inverse of above to do a swap in the location of the 2 values
                combo_list[num + 1] = position_1

sort_merged_lists(combo_list)

print("The sorted merged list of {} and {} is {}".format(sorted_list_1, sorted_list_2, combo_list))
# Resulting Output: [10, 10, 12, 12, 15, 15, 17, 17, 19, 21, 30]
