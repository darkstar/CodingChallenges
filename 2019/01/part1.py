total = 0

with open("input.txt", mode="r") as f:
    for line in f.readlines():
        x = int(line.strip())
        x = x // 3
        x -= 2
        total += x

print(total)
