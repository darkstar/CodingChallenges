with open("input.txt", mode="r") as f:
    code = list(map(int, f.readline().split(",")))

parts = [ [], [], [] ]

# split the ciphertext into 3 groups
for i in range(0, len(code), 3):
    parts[0].append(code[i])
    parts[1].append(code[i+1])
    parts[2].append(code[i+2])

# count the occurence of each number in each group, ignoring those that don't occur
counts = [ { i: parts[p].count(i) for i in range(256) if i in parts[p] } for p in range(3) ]

# get the number that has the maximum number of occurences
maximums = [ max(counts[i], key=counts[i].get) for i in range(3) ]

# assume that " " is the most common letter in each group
key = [ maximums[i] ^ ord(' ') for i in range(3) ]

# calculate the sum for each part separately
sums = [ sum([ x ^ key[i] for x in parts[i] ]) for i in range(3) ]

print(sum(sums))

for i in range(len(parts[0])):
    print("{}{}{}".format(*[ chr(parts[k][i]^key[k]) for k in range(3) ]), end='')

