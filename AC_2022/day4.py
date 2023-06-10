with open('C:/Users/Walker/Desktop/Advent_of_Code/AC_2022/data/input_day4.txt',"r") as f:
    data = [line.strip() for line in f]





k = 0 # It defined for counting the number of pairs that contains one another.

for i in data:

    # Here I do some arranging among the pairs,the gist of here is to get a set whose elements are the values that are given as one of the pair
    # when we get those sets,then,it will be easier to look at their intersection and count the given pairs that satisfy the given property...


    pair =  tuple(i.split(",")) 

    pair_first = tuple(pair[0].split("-"))
    pair_second = tuple(pair[1].split("-"))

    pair_first_set = set(range(int(pair_first[0]), int(pair_first[1])+1))
    pair_second_set = set(range(int(pair_second[0]), int(pair_second[1])+1))

    if (pair_first_set.intersection(pair_second_set) == pair_first_set) or (pair_first_set.intersection(pair_second_set) == pair_second_set):
        k += 1

print(k)

# 657


