floor = 0
index = 1
with open('input.txt', mode='r') as f:
    instructions = f.readlines()[0].rstrip()

    for ch in instructions:
        floor += { '(': 1, ')': -1}[ch]
        if floor == -1:
            print(index)
            exit(0)
        index += 1


