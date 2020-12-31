import re

r = re.compile('(?P<low>\d+)-(?P<high>\d+)\s+(?P<char>\S)\s*:\s*(?P<pw>\S*)$')

valid = 0

with open("input.txt", mode="r") as f:
    for l in f.readlines():
        m = r.match(l)
        vals = m.groupdict()
        # extract grups
        pw = vals['pw']          # password
        char = vals['char']      # rule char
        low = int(vals['low'])   # first character index
        high = int(vals['high']) # second character index

        ch1 = pw[low - 1]
        ch2 = pw[high - 1]

        if ((ch1 == char and ch2 != char) or (ch1 != char and ch2 == char)):
            valid += 1
        
print(valid)
