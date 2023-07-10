data = []
pos = 0
metadata_sum = 0

def readnode():
    global pos
    global data
    global metadata_sum

    children = int(data[pos])
    metadata = int(data[pos+1])
    pos += 2
    for x in range(children):
        readnode()
    for x in range(metadata):
        metadata_sum += int(data[pos])
        pos += 1

with open('input.txt', mode='r') as f:
    data = f.readlines()[0].rstrip().split()
    readnode()

print(metadata_sum)

