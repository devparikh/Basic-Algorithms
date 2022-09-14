# Problem 2691: Minimum Amount of Time to Collect Garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

metal_garbage_truck = []
paper_garbage_truck = []
glass_garbage_truck = []

garbage_list = ["MMM", "PGM", "GP"]
travel_list = [3,10]

total_time = 0
travel_count = -1

for house in garbage_list:
    garbage_collection_counter = -1
    for garbage_piece in house:
        if garbage_piece == "G":
            garbage_collection_counter += 1
            glass_garbage_truck.append(house[garbage_collection_counter])
            total_time += 1

            if garbage_collection_counter-1 >= 0:
                total_time += travel_list[garbage_collection_counter-1]

        elif garbage_piece == "M":
            garbage_collection_counter += 1
            metal_garbage_truck.append(house[garbage_collection_counter])
            total_time += 1

            if garbage_collection_counter-1 != 0:
                total_time += travel_list[garbage_collection_counter-1]

        else:
            garbage_collection_counter += 1
            paper_garbage_truck.append(house[garbage_collection_counter])
            total_time += 1

            if garbage_collection_counter-1 >= 0:
                total_time += travel_list[garbage_collection_counter-1]

print("The total amount of time it takes to pick up trash from {} houses is {} minutes".format(len(garbage_list), total_time))

