import re
import itertools # don't judge me :-D
import functools
import operator

def replaceat(s,idx,replacement):
    return '{}{}{}'.format(s[:idx],replacement,s[idx+1:])

def reversesub(s, beg, end):
    return s[0:beg] + s[beg:end+1][::-1] + s[end+1:]

def rol(s):
    return s[1:] + s[:1]

def ror(s):
    return s[-1:] + s[:-1]

with open("input.txt") as f:
    lines = f.readlines()

# generate a list of all possible password permutations
allpasswords = map(lambda x: functools.reduce(operator.add, x), itertools.permutations("abcdefgh"))

# prepare regexes
re1 = re.compile(r'swap position (\d+) with position (\d+)')
re2 = re.compile(r'swap letter (.) with letter (.)')
re3 = re.compile(r'rotate (left|right) (\d+) steps?')
re4 = re.compile(r'rotate based on position of letter (.)')
re5 = re.compile(r'reverse positions (\d+) through (\d+)')
re6 = re.compile(r'move position (\d+) to position (\d+)')

for passwd in allpasswords:
    # start with our initial password
    password = passwd
    for l in lines:
        # print("password is now {}".format(password))
        m = re1.match(l)
        if m:
            pos1 = int(m.group(1))
            pos2 = int(m.group(2))
            tmp = password[pos1]
            password = replaceat(password, pos1, password[pos2])
            password = replaceat(password, pos2, tmp)
            # print("  swapped positions {} and {}".format(pos1, pos2))
            continue

        m = re2.match(l)
        if m:
            ch1 = m.group(1)
            ch2 = m.group(2)
            password = password.replace(ch1, "#")
            password = password.replace(ch2, ch1)
            password = password.replace("#", ch2)
            # print("  swapped {} and {}".format(ch1, ch2))
            continue

        m = re3.match(l)
        if m:
            count = int(m.group(2))
            for x in range(count):
                password = rol(password) if m.group(1) == "left" else ror(password)
            # print("  rotated password {} by {}".format(m.group(1), count))
            continue

        m = re4.match(l)
        if m:
            ch = m.group(1)
            idx = password.index(ch)
            password = ror(password)
            for x in range(idx):
                password = ror(password)
            if idx >= 4:
                password = ror(password)
            # print("  rotated based on index of char {}".format(ch))
            continue

        m = re5.match(l)
        if m:
            a = int(m.group(1))
            b = int(m.group(2))
            password = reversesub(password, a, b)
            # print("  reversed from {} to {}".format(a, b))
            continue

        m = re6.match(l)
        if m:
            a = int(m.group(1))
            b = int(m.group(2))
            ch = password[a]
            # remove char at index a...
            password = password[:a] + password[a+1:]
            # and add it back into index b
            password = password[:b] + ch + password[b:]
            # print("  moved char from index {} to index {}".format(a, b))
            continue

        print("Unhandled line: {}".format(l))
        exit(1)
    if password == "fbgdceah":
        print(passwd)
        break
