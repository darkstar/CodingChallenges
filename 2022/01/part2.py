import itertools
import math

# read the input file
with open("input.txt", mode="r") as f:
    l = [x.strip() for x in f.readlines()]

elves = []
curr = []
# separate the list into groups separated by an empty string
while len(l) > 0:
    x = l[0]
    # non empty string?
    if len(x) > 0:
        # add to the calories of the current elf
        curr = curr + [int(x)]
    else:
        # store the previously collected elf's calorie data
        elves.append(curr)
        # start with a fresh elf
        curr = []
    l = l[1:]

# if we still have some calories, append it to the list
if len(curr) > 0:
    elves.append(curr)

# sum all calories
calories = list(map(lambda x: sum(x), elves))

calories.sort(reverse=True)

print(sum(calories[:3]))
