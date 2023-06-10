with open('C:/Users/Walker/Desktop/Advent_of_Code/AC_2022/data/input_day3.txt',"r") as f:
    data = [line.strip() for line in f]


import string

# setting up  the priority of the item types
lower_case_priority = dict(zip(list(string.ascii_lowercase), list(range(1,27))))

upper_case_priority = dict(zip(list(string.ascii_uppercase), list(range(27,59))))




# Find the item type that appears in both compartments of each rucksack

common_item_types = []

for j in data:
    temp_list = []

    first_compartment = j[:int(len(j)/2)]
    second_compartment = j[int(len(j)/2):]

    common_item_types.append(list(set(first_compartment).intersection(set(second_compartment))))


#  What is the sum of the priorities of those item types?

total = 0

for i in common_item_types:

    if i[0] in set(lower_case_priority.keys()):

        total += lower_case_priority[i[0]]
    
    elif i[0] in set(upper_case_priority):

        total += upper_case_priority[i[0]]

print(total)
# 8401

