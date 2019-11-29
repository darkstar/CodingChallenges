import math
from collections import defaultdict
from functools import reduce

target = 0
elf = 1

with open('input.txt', mode='r') as f:
    target = int(f.readlines()[0].rstrip())

presents = {}

def deliver(elf, house, number):
    cur = presents[house] if house in presents else 0
    cur += number
    presents[house] = cur
    if elf-1 in presents:
        if (presents[elf-1] >= target):
            print("Solution; {}".format(elf-1))
            exit(0)
        presents.pop(elf-1)

while True:
    for x in range(50):
        deliver(elf, (x + 1) * elf, 11 * elf)
    elf = elf + 1

