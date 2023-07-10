def b26dec(p):
    val = 0
    for x in p:
        val *= 26
        val += ord(x)-ord('a')
    return val

def b26enc(n):
    s = ""
    while n > 0:
        d = n % 26
        n //= 26
        s = chr(d + ord('a')) + s
    return s

def next(p):
    return b26enc(b26dec(p) + 1)

def valid(p):
    r1valid = False

    # rule 1
    for s in range(len(p)-2):
        (a,b,c) = (0, ord(p[s+1])-ord(p[s]), ord(p[s+2])-ord(p[s]))
        if (a,b,c) == (0,1,2):
            r1valid = True

    if not r1valid:
        return False

    # rule 2
    if 'l' in p or 'i' in p or 'o' in p:
        return False

    # rule #3
    dupes = {}
    for i in range(len(p) - 1):
        if p[i] == p[i+1]:
            dupes[p[i]] = True
            i += 1

    if len(dupes) < 2:
        return False

    return True

with open('input.txt', mode='r') as f:
    password = f.readlines()[0].rstrip()

    while not valid(password):
        password = next(password)

    password = next(password)
    while not valid(password):
        password = next(password)

print(password)
