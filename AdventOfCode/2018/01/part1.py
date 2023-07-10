
frequency = 0

with open('input.txt', mode='r') as f:
  lines = f.readlines()

  for line in lines:
      frequency += int(line)

print('Final frequency: ', frequency)

