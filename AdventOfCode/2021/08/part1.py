with open("input.txt", mode="r") as f:
  lines = [ x.strip() for x in f.readlines() ]

count = 0

for l in lines:
  inp, out = l.split("|")
  for d in out.strip().split():
    if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7:
      count = count + 1

print(count)
