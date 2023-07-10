from functools import reduce

def solved(bingo):
  # check rows
  for row in bingo:
    if all(list(map(lambda x: x == "x", row))):
      return True
  # check columns
  for col in range(5):
    c = [ r[col] for r in bingo ]
    if all(list(map(lambda x: x == "x", c))):
      return True
  return False

def markrow(row, num):
  return list(map(lambda x: "x" if x == num else x, row))

def mark(bingo, num):
  return list(map(lambda r: markrow(r, num), bingo))

def result(b, n):
  summ = reduce(lambda a, b: a + b, map(lambda a: int(a), filter(lambda x: x != "x", [ x for v in b for x in v ])))
  return summ * n

with open("input.txt", mode="r") as f:
  nums = f.readline().strip().split(",")
  rawbingos = [ x.strip() for x in f.readlines() ]

bingos = list(zip(*(iter(rawbingos),) * 6))

# drop the first line in each bingo
bingos = list(map(lambda x: x[1:], bingos))

# convert each row to a list
bingos = list(map(lambda x: list(map(lambda f: f.split(), x)), bingos))

for n in nums:
  # call out numbers and mark bingo boards
  newboards = []
  for b in bingos:
    # in every board, mark the number
    nextb = mark(b, n)
    if solved(nextb):
      print(result(nextb, int(n)))
      exit()
    newboards.append(nextb)
  bingos = newboards
