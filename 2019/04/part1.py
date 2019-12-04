
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
    if not se(n[0:2]) and not se(n[1:3]) and not se(n[2:4]) and not se(n[3:5]) and not se(n[4:6]):
        continue
    if ord(n[1]) < ord(n[0]) or ord(n[2]) < ord(n[1]) or ord(n[3]) < ord(n[2]) or ord(n[4]) < ord(n[3]) or ord(n[5]) < ord(n[4]):
        continue
    count += 1

print(count)
