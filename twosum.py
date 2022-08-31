import numpy as np

# Defining Two Sum Function
def twosum(nums_array, target):
  iteration_count = -1
  for integer in nums_array:
    iteration_count += 1
    # Don't execute this if statement if the current index is 0(which in CS is the first index) as it doesn't have a previous integer
    if iteration_count != 0:
      # Get the value of the previous integer
      prev_integer = nums_array[iteration_count - 1]
      # If the previous integer and the current integer's product is the target then print their indexes
      if prev_integer + integer == target:
        print("Integer #1 Index: {}".format(iteration_count - 1))
        print("Integer #2 Index: {}".format(iteration_count))

# Defining test array and target to test the algorithm
test_array = np.array([3, 7, 9, 5, 19, 80, 71, 100])
target = 171

twosum(test_array, target)
