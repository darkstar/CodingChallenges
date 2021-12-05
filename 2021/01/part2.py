with open("input.txt", mode="r") as f:
  depths = [ int(l) for l in f.readlines() ]

windows = [ depths[i+2] + depths[i+1] + depths[i] for i in range(len(depths)-2) ]
deltas = [ windows[i+1] - windows[i] for i in range(len(windows)-1) ]

print(len(list(filter(lambda x: x > 0, deltas))))
