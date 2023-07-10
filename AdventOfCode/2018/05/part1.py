
with open('input.txt',mode='r') as f:
  polymer = f.read(65536).rstrip()

  i = 0
  while i < len(polymer) - 1:
    (x, y) = (polymer[i], polymer[i+1])

    if ord(x) ^ ord(y) == 0x20:
      polymer = polymer[:i] + polymer[i+2::]
      if i > 0:
        i -= 1
    else:
      i += 1

print(len(polymer))    
