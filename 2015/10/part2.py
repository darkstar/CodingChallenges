def next(s):
    i = 0
    result = ""

    while len(s) > 0:
        c = s[0]
        prefix = ""
        while len(s) > 0 and s[0] == c:
            prefix += s[0]
            s = s[1:]
        result += str(len(prefix)) + c

    return result

with open('input.txt', mode='r') as f:
    line = f.readlines()[0].rstrip()

    for x in range(50):
        print("step {}: len={}".format(x, len(line)))
        line = next(line)

print(len(line))
