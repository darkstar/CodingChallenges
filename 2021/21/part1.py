die = 1
dierolls = 0
def roll():
  global die, dierolls
  v = die
  die = die + 1
  if die > 100:
    die = 1
  dierolls = dierolls + 1
  return v

def roll3():
  return roll() + roll() + roll()

with open("input.txt", mode="r") as f:
  p1 = int(f.readline().split()[-1]) - 1
  p2 = int(f.readline().split()[-1]) - 1

#p1 = 4 - 1
#p2 = 8 - 1
p = [p1, p2]
score = [0, 0]
player = 0

while True:
  r = roll3()
  p[player] = (p[player] + r) % 10
  sc = p[player] + 1
  score[player] = score[player] + sc
#  print("Player {} rolls {} and moves to space {} for a total score of {}".format(player+1, r, p[player]+1, score[player]))
  if score[player] >= 1000:
    break
  player = 1 - player

print(score[1-player]*dierolls)
