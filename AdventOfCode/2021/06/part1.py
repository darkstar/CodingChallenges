with open("input.txt", mode="r") as f:
  fish = [ int(l) for l in f.readline().strip().split(",") ]

#fish = [ 3, 4, 3, 1, 2 ]

day = 0

# brute force simulation

while True:
  day += 1
  newfish = []
  for i in range(len(fish)):
    if fish[i] == 0:
      newfish.append(8)
      fish[i] = 6
    else:
      fish[i] = fish[i] - 1
  fish = fish + newfish
  if day==80:
    break

print(len(fish))
