from functools import reduce

with open("input.txt", mode="r") as f:
  rawfish = [ int(l) for l in f.readline().strip().split(",") ]

#rawfish = [ 3, 4, 3, 1, 2 ]

fish = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0 }
for x in rawfish:
  fish[x] = fish[x] + 1

day = 0

# smart simulation

while True:
  day += 1
  newfish = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0 }
  for age in range(1, 9):
    newfish[age - 1] = fish[age]
  newfish[8] = fish[0]
  newfish[6] += fish[0]
  fish = newfish

  if day==256:
    break

count = reduce(lambda x, key: x + fish[key], fish, 0)

print(count)
