
frequency = 0
frequencies = {}

while True:
  with open('input.txt', mode='r') as f:
    lines = f.readlines()
  
    for line in lines:
        if frequency in frequencies:
            print('Duplicate frequency found: ', frequency)
            exit(1)

        frequencies[frequency] = 1
        frequency += int(line)
