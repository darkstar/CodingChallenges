result = 0

with open("input.txt") as f:
    while l := f.readline():
        s = "".join(c for c in l if c in "0123456789")
        result += int(s[0] + s[-1])

print(result)
