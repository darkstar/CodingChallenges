score = 0

with open("input.txt", mode="r") as f:
    for s in f.readlines():
        s1, s2 = set(s[:len(s)//2]), set(s[len(s)//2:])
        c = s1.intersection(s2).pop()
        if c.islower():
            score += ord(c) - ord('a') + 1
        if c.isupper():
            score += ord(c) - ord('A') + 27

print(score)
