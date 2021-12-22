from itertools import product

def dirac(p1, p2, s1, s2, player, cache):
  # check memoization cache
  if (p1, p2, s1, s2, player) in cache:
    return cache[(p1, p2, s1, s2, player)]

  wins = [0, 0]
  # generate list of possible triple dice rolls
  rolls = list(map(sum, product([1, 2, 3], repeat=3)))

  for r in rolls:
    pos = [p1, p2]
    score = [s1, s2]

    # calculate new position and score after this round
    pos[player] = (pos[player] + r - 1) % 10 + 1
    score[player] += pos[player]

    # check wins
    if score[player] >= 21:
      # this was the finishing game
      wins[player] += 1
    else:
      # recursive depth-first search
      w1, w2 = dirac(pos[0], pos[1], score[0], score[1], 1 - player, cache)

      wins[0] += w1
      wins[1] += w2

  # after looping all dice results: cache the number of wins
  cache[(p1, p2, s1, s2, player)] = wins
  return wins

with open("input.txt", mode="r") as f:
  pos = list(map(lambda s: int(s.strip().split()[-1]), f.readlines()))

# pos = [4, 8]
print(max(dirac(pos[0], pos[1], 0, 0, 0, {})))
