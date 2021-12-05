with open("input.txt", mode="r") as f:
  data = [ x.strip() for x in f.readlines() ]

numbits = len(data[0])
gamma = ""
epsilon = ""

for b in range(numbits):
  bits = list(map(lambda x: x[b], data))
  ones = list(filter(lambda x: x == "1", bits))
  zeroes = list(filter(lambda x: x == "0", bits))
  if len(zeroes) > len(ones):
    gamma = gamma + "0"
    epsilon = epsilon + "1"
  else:
    gamma = gamma + "1"
    epsilon = epsilon + "0"

print(int(gamma, 2) * int(epsilon, 2))

