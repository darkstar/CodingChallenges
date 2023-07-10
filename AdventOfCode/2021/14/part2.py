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

pairs = { p: poly.count(p) for p in rules }
counts = { c: poly.count(c) for c in rules.values() }

step = 1
while True:
  if step > 40:
    break
  pairs2 = pairs.copy()
  for p, v in pairs2.items():
    pairs[p] -= v # we replace this pair v times
    pairs[p[0] + rules[p]] += v # the first pair we add
    pairs[rules[p] + p[1]] += v # the second pair we add
    counts[rules[p]] += v # we added the new character v times
  step += 1

v1 = max(counts.values())
v2 = min(counts.values())
print(v1 - v2)
