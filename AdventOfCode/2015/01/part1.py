floor = 0

with open('input.txt', mode='r') as f:
    instructions = f.readlines()[0].rstrip()

    for ch in instructions:
        floor += { '(': 1, ')': -1}[ch]

print(floor)

