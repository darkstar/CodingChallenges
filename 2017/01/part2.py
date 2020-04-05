
with open("input.txt") as f:
    s = f.readline().strip()

total = 0
for x in range(len(s)):
    if s[x] == s[(x + len(s) // 2) % len(s)]:
        total += int(s[x])

print(total)
