import re

# brute force. don't judge me :-P

with open("input.txt") as f:
    elves = int(f.readlines()[0].strip())

# elves = 5

presents = [ 1 ] * elves

elvesleft = elves
pos = 0

while True:
    # jump to next remaining elf
    while presents[pos] == 0:
        pos = (pos + 1) % elves
    
    # find the next elf
    nextelf = (pos + 1) % elves
    while presents[nextelf] == 0:
        nextelf = (nextelf + 1) % elves
    
    # take all the presents of the next elf
    presents[pos] += presents[nextelf]
    presents[nextelf] = 0
    
    # eliminate the next elf
    elvesleft -= 1
    
    # print status
    # print("elf {} takes all presents from elf {}, bringing him up to {}. Elves left: {}".format(pos + 1, nextelf + 1, presents[pos], elvesleft))

    # exit if only one elf left
    if elvesleft == 1:
        break

    # go to the next elf
    pos = (pos + 1) % elves

print(pos + 1)
