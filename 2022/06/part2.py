def distinct(s, n):
    for i in range(n, len(s)):
        mark = s[i-n:i]
        if len(set(mark)) == n:
            return i
    return None

def sop(s):
    return distinct(s, 4)

def som(s):
    return distinct(s, 14)

code = open("input.txt", mode="r").readline().strip()

print(som(code))
