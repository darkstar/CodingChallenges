def tokenize(s):
  r = []
  i = 0
  s = s.strip()
  while i < len(s):
    # skip whitespace
    if s[i] == " ":
      i += 1
      continue
    if s[i] in [ '(', ')', '+', '*']:
      r.append(s[i])
      i += 1
      continue
    if s[i] in "0123456789":
      num = ""
      while i < len(s) and s[i] in "0123456789":
        num = num + s[i]
        i += 1
      r.append(int(num))
      continue
  return r

# "easy" math: all operators have the same precedence
#
# BNF:
# expr = term [ { "+","*" } term ]
# term = number | "(" expr ")"

tok = []

def term():
  global tok
#  print("term({})".format(tok))
  if len(tok) == 0:
    print("stack underflow")
    exit(1)
  if isinstance(tok[0], int):
    r = tok[0]
    tok = tok[1:]
    return r
  if tok[0] == '(':
    tok = tok[1:]
    r = expr()
    if tok[0] != ')':
      print("missing ')'")
      exit(1)
    else:
      tok = tok[1:]
    return r
  print("unknown term: {}".format(tok))
  exit(1)

def expr():
  global tok
#  print("expr({})".format(tok))
  r = term()
  while len(tok) > 0 and tok[0] != ')':
    if isinstance(tok[0], int):
      print("expected operator")
      exit(1)
    op = tok[0]
    tok = tok[1:]
    r2 = term()
    if op == "+": r = r + r2
    if op == "*": r = r * r2
  return r

#tests = [
#  ("2 * 3 + (4 * 5)", 26),
#  ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
#  ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
#  ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632)
#]
#
#for (s, x) in tests:
#  print(s)
#  tok = tokenize(s)
#  res = expr()
#  print(res)
#  if res != x:
#    print("Error, expected {}".format(x))
#  print("----")

with open("input.txt", mode="r") as f:
  lines = [x.strip() for x in f.readlines()]

result = 0
for l in lines:
  tok = tokenize(l)
  result += expr()

print(result)
