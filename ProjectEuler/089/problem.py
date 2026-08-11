numerals = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

# we assume the number is well-formed and passes all rules
def parse_roman(s):
    n = 0
    for i in range(len(s)):
        v = numerals[s[i]]

        # if we are not at the end
        if i < len(s) - 1:
            # check next numeral for adding or subtracting
            v2 = numerals[s[i+1]]

            if v < v2:
                n -= v
            else:
                n += v
        else:
            # last is always positive
            n += v
    return n

# ugly but works :)
def gen_roman(n):
    s = ""
    while n >= 1000:
        s += "M"
        n -= 1000
    while n >= 900:
        s += "CM"
        n -= 900
    while n >= 500:
        s += "D"
        n -= 500
    while n >= 400:
        s += "CD"
        n -= 400
    while n >= 100:
        s += "C"
        n -= 100
    while n >= 90:
        s += "XC"
        n -= 90
    while n >= 50:
        s += "L"
        n -= 50
    while n >= 40:
        s += "XL"
        n -= 40
    while n >= 10:
        s += "X"
        n -= 10
    while n >= 9:
        s += "IX"
        n -= 9
    while n >= 5:
        s += "V"
        n -= 5
    while n >= 4:
        s += "IV"
        n -= 4
    while n >= 1:
        s += "I"
        n -= 1
    return s

result = 0

with open("input.txt", mode="r") as f:
    lines = [ x.strip() for x in f.readlines() ]

    for s in lines:
        l1 = len(s)
        l2 = len(gen_roman(parse_roman(s)))
        delta = l1 - l2
        result += delta

print(result)
