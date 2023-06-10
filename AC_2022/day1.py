with open('C:/Users/Walker/Desktop/Advent_of_Code/AC_2022/data/input_day1.txt',"r") as f:
    data = [line.strip() for line in f]

# print(data)


elves = []
total_calories = 0

# Iterate over the data and keep track of the total number of Calories for each Elf
for calories in data:
    # If we encounter a blank line, start a new Elf
    if calories != "":
        total_calories += int(calories)

    else:
        elves.append(total_calories)
        total_calories = 0

print(max(elves))
# 66719

order = dict(zip(elves ,tuple(range(1,len(elves) + 1))))

print(order[max(elves)])
# 180





