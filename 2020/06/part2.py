with open("input.txt", mode="r") as f:
    groups = f.read().strip().split("\n\n")

answers = list(map(lambda x: (x.split("\n"), set("".join(x.split("\n")))), groups))

result = 0

for g, s in answers:
    # g is the list of answers given by everyone in the group
    # s is the letters that appear in any answer (part 1)

    # for each letter in s, find out if all group answers contain that letter
    a = list(map(lambda x: all(map(lambda y: x in y, g)), s))

    # count the number of "True" elements in a
    num = len(list(filter(lambda x: x, a)))

    result += num

print(result)
