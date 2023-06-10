"""
(You can go to the page of Advent of Code to see the whole problem statement)

A for Rock, B for Paper, and C for Scissors. The second column--" 
Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response:
X for Rock, Y for Paper, and Z for Scissors. Winning every time
would be suspicious, so the responses must have been carefully chosen.
"""


with open('C:/Users/Walker/Desktop/Advent_of_Code/AC_2022/data/input_day2.txt',"r") as f:
    data = [line.strip() for line in f]




total_score = 0


for i in data:
    # round that there is no winner;
    if (i[0] == "A") and (i[-1] == "X"):
        total_score += 1 + 3
    elif (i[0] == "B") and (i[-1] == "Y"):
        total_score += 2 + 3
    elif (i[0] == "C") and (i[-1] == "Z"):
        total_score += 3 + 3
    # round that we win;
    elif (i[0] == "A") and (i[-1] == "Y"):
        total_score += 2 + 6
    elif (i[0] == "B") and (i[-1] == "Z"):
        total_score += 3 + 6
    elif (i[0] == "C") and (i[-1] == "X"):
        total_score += 1 + 6
    # round that we lose;
    elif (i[0] == "A") and (i[-1] == "Z"):
        total_score += 3 
    elif (i[0] == "B") and (i[-1] == "X"):
        total_score += 1 
    elif (i[0] == "C") and (i[-1] == "Y"): 
        total_score += 2 


print(total_score)

# 13268

