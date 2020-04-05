fw = {}

with open("input.txt") as f:
    for line in f.readlines():
        pfilter = line.strip().split(": ")
        fw[int(pfilter[0])] = { "depth": int(pfilter[0]), "range": int(pfilter[1]), "cur": 0 , "dir": 1 }

last = int(pfilter[0])

# for testing
#fw = { 0: { "depth": 0, "range": 3, "cur": 0, "dir": 1},
#       1: { "depth": 1, "range": 2, "cur": 0, "dir": 1},
#       4: { "depth": 4, "range": 4, "cur": 0, "dir": 1},
#       6: { "depth": 6, "range": 4, "cur": 0, "dir": 1}}
#       last = 6

layer = 0
severity = 0
while layer < last:
    # check if we have a filter at the current position
    if layer in fw:
        # check if the packet moved into a controlled layer
        flt = fw[layer]
        if flt["cur"] == 0:
            severity += flt["range"] * flt["depth"]
    # move all filters
    for flt in fw:
        fw[flt]["cur"] = fw[flt]["cur"] + fw[flt]["dir"]
        # invert movement direction if we hit the end
        if fw[flt]["cur"] == 0 or fw[flt]["cur"] == fw[flt]["range"] - 1:
            fw[flt]["dir"] *= -1

    # move to the next layer
    layer += 1

print(severity)
