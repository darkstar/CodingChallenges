# yes, I know, this is cheating a little bit...
from lark import Lark
import sys

ruleset = ""
with open("input.txt", mode="r") as f:
  l = f.readline().strip()
  while len(l) > 0:
    # rule
    rule = ""
    x = l.split(":")
    if x[1].strip().startswith('"'):
      # terminal
      rule = "rule{}: {}".format(x[0], x[1].strip())
    else:
      alts = x[1].split('|')
      alts = " | ".join([ " ".join(map(lambda k: "rule{}".format(k), v.split())) for v in x[1].split("|") ])
      rule = "rule{}: {}".format(x[0], alts)
    ruleset += rule + "\n"
    l = f.readline().strip()

  # rest is the data
  data = f.readlines()

ruleset=ruleset.replace("rule0:", "start:")

parser = Lark(ruleset)

valid = 0
for d in data:
  try:
    parser.parse(d.strip())
    valid = valid + 1
  except:
    pass

print(valid)
