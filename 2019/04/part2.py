
with open("input.txt", mode="r") as f:
    vals = f.readline().strip().split("-")
    startval = vals[0]
    endval = vals[1]

count = 0

#stringequal - return True if string consists of the same characters
def se(s):
    for x in range(len(s) - 1):
        if s[x] != s[x + 1]: return False
    return True

for x in range(int(startval), int(endval) + 1):
    n = "{}".format(x)
    if ord(n[1]) < ord(n[0]) or ord(n[2]) < ord(n[1]) or ord(n[3]) < ord(n[2]) or ord(n[4]) < ord(n[3]) or ord(n[5]) < ord(n[4]):
        continue
    if ((se(n[0:2]) and n[0] != n[2]) or
        (se(n[1:3]) and (n[1] != n[0] and n[1] != n[3])) or
        (se(n[2:4]) and (n[2] != n[1] and n[2] != n[4])) or
        (se(n[3:5]) and (n[3] != n[2] and n[3] != n[5])) or
        (se(n[4:6]) and n[4] != n[3])):
        count += 1

print(count)
