
def unclength(data):
    length = 0
    index = 0
    output = []
    while index < len(data):
        if data[index] == '(':
            index += 1
            marker = []
            while data[index] != ')':
                marker.append(data[index])
                index += 1
            index += 1 # skip final ")"
            m = "".join(marker).split("x")
            l = int(m[0])
            r = int(m[1])
            cdata = data[index:index+l]
            length += r * unclength(cdata)
            index += l - 1
        else:
            length += 1
        index += 1

    return length

with open("input.txt", mode="r") as f:
    data = f.readline().strip()
    output = unclength(data)

print(output)

