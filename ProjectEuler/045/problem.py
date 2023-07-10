t = 1
p = 1
h = 1
tn = 1
pn = 1
hn = 1

while True:
    # next hexagonal number
    hn += 1
    h = hn * (2 * hn - 1)

    # search next pent. number at least as large as h
    while p < h:
        pn += 1
        p = (pn * (3 * pn - 1)) // 2

    # search next tri. number at least as large as h
    while t < h:
        tn += 1
        t = (tn * (tn + 1)) // 2

    if t == p and p == h:
        if t > 40755:
            print(t)
            break

