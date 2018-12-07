import re

def is_nice(s):
    if re.search('(ab|cd|pq|xy)', s):
        return False

    if sum([s.count(x) for x in 'aiueo']) < 3:
        return False

    if not re.search('(.)\\1', s):
        return False

    return True

with open('input.txt', mode='r') as f:
    words = [x.rstrip() for x in f.readlines()]

    nicewords = [w for w in words if is_nice(w)]

print(len(nicewords))

