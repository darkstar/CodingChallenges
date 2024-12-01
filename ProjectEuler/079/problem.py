with open("input.txt", mode="r") as f:
    codes = [ x.strip() for x in f.readlines() ]

code = codes[0]
codes = codes[1:]

for y in codes:
    if code[:2] == y[1:]:
        # 1234567, 912 -> 91234567
        code = y[0] + code
    elif code[-2:] == y[:2]:
        # 1234567, 679 -> 12345679
        code = code + y[2]
    elif code[0] == y[2]:
        # 1234567, 981 -> 981234567
        code = y[:2] + code
    elif code[-1] == y[0]:
        # 1234567, 789 -> 123456789
        code = code + y[1:]
    else:
        # 1234567, 495 -> 12349567
        # or ignore if no match
        code = code.replace(y[0]+y[2], y)

print(code)
