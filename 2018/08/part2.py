data = []
pos = 0

def readnode():
    global pos
    global data
    
    msum = 0
    csums = {}
    mdata = []

    numchildren = int(data[pos])
    nummetadata = int(data[pos+1])

    pos += 2

    for x in range(numchildren):
        csums[x + 1] = readnode()

    for x in range(nummetadata):
        msum += int(data[pos])
        mdata.append(int(data[pos]))
        pos += 1

    if numchildren == 0:
        return msum
    else:
        val = 0
        for m in mdata:
            if m in csums:
                val += csums[m]
        return val

with open('input.txt', mode='r') as f:
    data = f.readlines()[0].rstrip().split()
    val = readnode()

print(val)

