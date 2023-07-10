import itertools

result = 0

for n in itertools.permutations('0123456789'):
    s = "".join(n)
    if int(s[1:4]) % 2 != 0:
        continue
    if int(s[2:5]) % 3 != 0:
        continue
    if int(s[3:6]) % 5 != 0:
        continue
    if int(s[4:7]) % 7 != 0:
        continue
    if int(s[5:8]) % 11 != 0:
        continue
    if int(s[6:9]) % 13 != 0:
        continue
    if int(s[7:10]) % 17 != 0:
        continue

    result += int(s)

print(result)
