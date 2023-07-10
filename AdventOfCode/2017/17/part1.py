with open("input.txt") as f:
    steps = int(f.readline().strip())

buf = [ 0 ]
pos = 0

for x in range(1, 2018):
    # step ahead
    pos = (pos + steps) % len(buf)
    # insert new value
    buf.insert(pos + 1, x)
    # step ahead
    pos += 1

print(buf[pos + 1])
