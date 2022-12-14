# Iterative Implementation of Binary Search
# Time Complexity - O(log n)
input_list = [1, 3, 7, 1024, 902, 13, 134]

target_value = 134

sorted_list = sorted(input_list)
original_list = sorted_list

def binary_search(sorted_test_list, target_value, original_list):
    value_found = False
    while value_found == False:
        if len(sorted_test_list) != 0:
            middle_element = int((len(sorted_test_list) - 1)/2)
            if target_value == sorted_test_list[middle_element]:
                item = original_list.index(target_value) + 1 
                value_found = True
                print("The index of the element {} is {}.".format(target_value, item))
                break

            if target_value < sorted_test_list[middle_element]:
                sorted_test_list = sorted_test_list[0:middle_element]
                
            elif target_value > sorted_test_list[middle_element]:
                sorted_test_list = sorted_test_list[middle_element+1:len(sorted_test_list)]
        else:
            print("The value {} is not present in the input list.".format(target_value))
            break
        
binary_search(sorted_list, target_value, original_list)
