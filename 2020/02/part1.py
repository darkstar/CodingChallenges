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
        low = int(vals['low'])   # minimum occurences
        high = int(vals['high']) # maximum occurences
        num = pw.count(char)     # actual occurences
        if num >= low and num <= high:
            valid += 1
        
print(valid)
