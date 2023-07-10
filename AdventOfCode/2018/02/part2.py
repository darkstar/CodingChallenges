
def hammingdist(a, b):
  return len(list(filter(lambda t: t[0] != t[1], zip(a,b))))

with open('input.txt', mode='r') as f:
  lines = f.readlines()

  for i in range(0, len(lines) - 1):
    for j in range(i + 1, len(lines)):
      if hammingdist(lines[i], lines[j]) == 1:
        print(''.join(list(map(lambda t: t[0], filter(lambda tup: tup[0]==tup[1],zip(lines[i],lines[j]))))))
        exit()

