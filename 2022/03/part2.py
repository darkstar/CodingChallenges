score = 0

with open("input.txt", mode="r") as f:
    s = [ x.strip() for x in f.readlines() ]
    for i in range(0, len(s), 3):
        s1, s2, s3 = set(s[i]), set(s[i+1]), set(s[i+2])
        c = s1.intersection(s2).intersection(s3).pop()
        if c.islower():
            score += ord(c) - ord('a') + 1
        if c.isupper():
            score += ord(c) - ord('A') + 27

print(score)
