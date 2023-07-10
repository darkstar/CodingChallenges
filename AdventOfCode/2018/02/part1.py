
lettercounts = {}
twoletter = 0
threeletter = 0

with open('input.txt', mode='r') as f:
  lines = f.readlines()

  for line in lines:
    # read the chars into a dict
    lettercounts.clear()
    for ch in line:
      if ch in lettercounts:
        lettercounts[ch] += 1;
      else:
        lettercounts[ch] = 1;

    # check for double/triple chars
    if 2 in lettercounts.values():
      twoletter+=1

    if 3 in lettercounts.values():
      threeletter+=1

print('Checksum: ', twoletter * threeletter)

