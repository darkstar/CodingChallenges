from functools import reduce

def fn(state, cmd):
  (x, y) = state
  if cmd[0] == "forward":
    return (x + cmd[1], y)
  if cmd[0] == "up":
    return (x, y - cmd[1])
  if cmd[0] == "down":
    return (x, y + cmd[1])
  print("invalid command '{}'".format(cmd[0]))
  return (x, y)

with open("input.txt", mode="r") as f:
  cmds = list(map(lambda a: (a[0], int(a[1])), [ x.strip().split(" ") for x in f.readlines() ]))

pos = reduce(fn, cmds, (0, 0))
print(pos[0] * pos[1])

