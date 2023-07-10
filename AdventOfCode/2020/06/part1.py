with open("input.txt", mode="r") as f:
    groups = f.read().split("\n\n")

sets = map(lambda x: len(set("".join(x.split("\n")))), groups)

print(sum(sets))
