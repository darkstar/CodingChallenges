
def uncompress(data):
    index = 0
    output = []
    while index < len(data):
        if data[index] == '(':
            index += 1
            marker = []
            # decompress
            while data[index] != ')':
                marker.append(data[index])
                index += 1
            index += 1 # skip final ")"
            m = "".join(marker).split("x")
            l = int(m[0])
            r = int(m[1])
            cdata = data[index:index+l]
            for x in range(r):
                output.extend(list(cdata))
            index += l - 1
        else:
            output.append(data[index])
        index += 1

    return "".join(output)

with open("input.txt", mode="r") as f:
    data = f.readline().strip()
    output = uncompress(data)

print(len(output))

