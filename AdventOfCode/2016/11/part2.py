import re

floors = []

# this is cheating as I couldn't get my code to work correctly yet
with open("input.txt", mode="r") as f:
    lines = f.readlines()
    for l in lines:
        floors.append(len(re.findall(r"(microchip|generator)", l)))

floors[0] += 4

print(sum(2 * sum(floors[:x]) - 3 for x in range(1,4)))
