with open("input.txt", mode="r") as f:
  data = [ x.strip() for x in f.readlines() ]

#data = [
#"00100",
#"11110",
#"10110",
#"10111",
#"10101",
#"01111",
#"00111",
#"11100",
#"10000",
#"11001",
#"00010",
#"01010"]

numbits = len(data[0])

def mostcommon(b):
  ones = list(filter(lambda x: x == "1", b))
  zeroes = list(filter(lambda x: x == "0", b))
  return "1" if len(ones) >= len(zeroes) else "0"

def leastcommon(b):
  ones = list(filter(lambda x: x == "1", b))
  zeroes = list(filter(lambda x: x == "0", b))
  return "0" if len(zeroes) <= len(ones) else "1"

# make copies of our list to start with
csr = data.copy()
ogr = data.copy()

for b in range(numbits):
  # find the most and least common
  mcbits = list(map(lambda x: x[b], ogr))
  lcbits = list(map(lambda x: x[b], csr))
  mc = mostcommon(mcbits)
  lc = leastcommon(lcbits)
  # check ogr (most common)
  if len(ogr) > 1:
    ogr = list(filter(lambda x: x[b] == mc, ogr))
  # check lgr (least common)
  if len(csr) > 1:
    csr = list(filter(lambda x: x[b] == lc, csr))

  if len(ogr) == 1 and len(csr) == 1:
    break

print(int(ogr[0], 2) * int(csr[0], 2))

