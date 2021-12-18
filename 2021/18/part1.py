from functools import reduce

def parse(s):
  level = 0
  res = []
  i = 0
  while i < len(s):
    if s[i] == "[":
      i += 1
      level += 1
    elif s[i] == "]":
      i += 1
      level -= 1
    elif s[i] == ",":
      i += 1
    else:
      num = ""
      while s[i] in "0123456789":
        num += s[i]
        i += 1
        if i >= len(s):
          break
      res.append((int(num), level))
  return res

def explode(l):
  for i in range(len(l)):
    if l[i][1] != 5:
      continue
    # explode this pair
    left = l[i]
    right = l[i+1]
    if i > 0:
      l[i-1] = (l[i-1][0] + left[0], l[i-1][1])
    if i+1 < len(l) - 1:
      l[i+2] = (l[i+2][0] + right[0], l[i+2][1])

    # result is left part unchanged, then the new 0 value one level higher,
    # then one element is removed and then the right part of the list unchanged
    return l[:i] + [(0, l[i][1] - 1)] +  l[i+2:], True
  return l, False

def split(l):
  for i in range(len(l)):
    if l[i][0] > 9:
      v1 = l[i][0] // 2
      v2 = l[i][0] - v1
      return l[:i] + [ (v1, l[i][1] + 1), (v2, l[i][1] + 1)] + l[i + 1:], True
  return l, False

def red(l):
  while True:
    l, changed = explode(l)
    if changed:
      continue
    l, changed = split(l)
    if changed:
      continue
    break

  return l

def add(a,b):
  result = []
  for x in a:
    result.append((x[0], x[1] + 1))
  for x in b:
    result.append((x[0], x[1] + 1))
  return red(result)

def magn(l):
  while True:
    maxdepth = max([x for (_, x) in l])
    if maxdepth == 0:
      return l[0][0]
    # find index of maxdepth
    for i in range(len(l)):
      if l[i][1] == maxdepth:
        break
    # calculate magnitude
    mag = 3 * l[i][0] + 2 * l[i+1][0]
    l = l[:i] + [ (mag, l[i][1] - 1) ] + l[i+2:]

with open("input.txt", mode="r") as f:
  a0 = parse(f.readline().strip())
  an = list(map(lambda x: parse(x), [ y.strip() for y in f.readlines() ]))

print(magn(reduce(lambda a,b: add(a, b), an, a0)))

