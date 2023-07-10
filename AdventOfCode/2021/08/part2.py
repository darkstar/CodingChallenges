def minus(s1, s2):
  """ returns string s1 "minus" s2 """
  res = ""
  for x in s1:
    if not x in s2:
      res += x
  return res

def convert(s, segs):
  """ converts segments in s to "correct" segments via mapping in segs """
  res = ""
  for c in s:
    res = res + segs[c]
  return "".join(sorted(res))

def tonum(l):
  """ converts a list of "correct" segments to its decimal representation """
  nums = { "abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9 }
  digits = "".join(map(lambda f: str(nums[f]), l))

  return int(digits)

with open("input.txt", mode="r") as f:
  lines = [ x.strip() for x in f.readlines() ]

#lines = [ "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf" ]

total = 0

for l in lines:
  segments = {} # key: renamed segment, value: actual "correct" segment
  inp, out = l.split("|")
  inp = list(map(lambda f: "".join(sorted(f)), inp.split()))

  one = list(filter(lambda f: len(f) == 2, inp))[0]
  seven = list(filter(lambda f: len(f) == 3, inp))[0]
  four = list(filter(lambda f: len(f) == 4, inp))[0]
  # segment a is the difference between 1 and 7
  a = minus(seven, one)
  segments[a] = "a" 
  # count the segments
  counts = { 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0 }
  for n in inp:
    for seg in n:
      counts[seg] = counts[seg] + 1
  # segment b is on exactly 6 times
  b = [ x for x in counts.keys() if counts[x] == 6 ][0]
  segments[b] = "b"
  # segment e is on exaxctly 4 times
  e = [ x for x in counts.keys() if counts[x] == 4 ][0]
  segments[e] = "e"
  # segment f is on exaxctly 9 times
  f = [ x for x in counts.keys() if counts[x] == 9 ][0]
  segments[f] = "f"
  # segment c is on exactly 8 times, same as segment a, but we have a already
  c = [ x for x in counts.keys() if counts[x] == 8 and x != a ][0]
  segments[c] = "c"
  # segment d is on in the number 4, so find that by removing
  # segments b, c and f from the uniquely determined number 4
  d = minus(four, b+c+f)
  segments[d] = "d"
  # segment g is the last remaining
  g = minus("abcdefg", a+b+c+d+e+f)
  segments[g] = "g"

  total = total + tonum(map(lambda x: convert(x, segments), out.split()))

print(total)
