result = 0

def repl(s):
    r = ""

    tbl = { "one": "1", "two": "2", "three": "3",
            "four": "4", "five": "5", "six": "6",
            "seven": "7", "eight": "8", "nine": "9" }
    for i in range(len(s)):
        found = False
        for k, v in tbl.items():
            if s[i:].startswith(k):
                r += v
                i += len(k) - 1
                found = True
                break
        if not found:
            r += s[i]

    return r

with open("input.txt") as f:
    while l := f.readline():
        l = repl(l)
        s = "".join(c for c in l if c in "0123456789")
        if len(s)== 0:
            print(l)
        result += int(s[0] + s[-1])

print(result)
