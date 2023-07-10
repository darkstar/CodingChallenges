with open("input.txt", mode="r") as f:
  depths = [ int(l) for l in f.readlines() ]

deltas = [ depths[i+1] - depths[i] for i in range(len(depths)-1) ]

print(len(list(filter(lambda x: x > 0, deltas))))
