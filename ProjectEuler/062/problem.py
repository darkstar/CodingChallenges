d = {}

for n in range(1, 50000):
    cube = n * n * n
    digits = "".join(sorted(list(str(cube))))
    if digits in d:
        d[digits] += [cube]
        if len(d[digits]) == 5:
            print(d[digits][0])
            break
    else:
        d[digits] = [cube]


