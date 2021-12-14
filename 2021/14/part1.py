with open("input.txt", mode="r") as f:
  poly = f.readline().strip()
  f.readline()
  xrules = [ x.strip() for x in f.readlines() ]

#poly = "NNCB"
#xrules = [ "CH -> B", "HH -> N", "CB -> H", "NH -> C", "HB -> C", "HC -> B",
#"HN -> C", "NN -> C", "BH -> H", "NC -> B", "NB -> B", "BN -> B", "BB -> N",
#"BC -> B", "CC -> N", "CN -> C"]

xrules = list(map(lambda s: s.split(), xrules))
rules = {}
for x in xrules:
  rules[x[0]] = x[2]

step = 1
while True:
  if step > 10:
    break
  # build new polymer
  new = ""
  for i in range(len(poly) - 1):
    pair = poly[i:i+2]
    new = new + pair[0]
    if pair in rules:
      new = new + rules[pair]
  new = new + poly[-1]
  poly = new
  step = step + 1

# count items
counts = {}
for x in poly:
  if not x in counts:
    counts[x] = 0
  counts[x] = counts[x] + 1

v1 = max(counts.values())
v2 = min(counts.values())
print(v1 - v2)
