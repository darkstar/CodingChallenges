with open("input.txt", mode="r") as f:
    jolts = [ int(x.strip()) for x in f.readlines() ]

jolts.sort()

results = { 0: 1 }

# append target value
jolts += [ jolts[-1] + 3]

for j in jolts:
    results[j] = results.get(j - 3, 0) + results.get(j - 2, 0) + results.get(j - 1, 0)

print(results[jolts[-1]])
