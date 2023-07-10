
with open("input.txt", mode="r") as f:
    names = [ x.strip('"') for x in f.readline().split(",") ]

names.sort()

result = 0

for i in range(len(names)):
    n = sum(map(lambda x: ord(x) - ord('A') + 1, list(names[i]))) * (i + 1)

    result += n

print(result)
