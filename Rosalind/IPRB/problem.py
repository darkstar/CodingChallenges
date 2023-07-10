import itertools

# solved by simulation, not by calculation ;-)
def solution(ifile):
    with open(ifile, mode="r") as f:
        k, m, n = map(int, f.readline().strip().split(" "))

    pop = "D" * k + "H" * m + "R" * n

    total = 0
    pheno = 0
    for c in itertools.permutations(range(len(pop)), 2):
        i1 = pop[c[0]]
        i2 = pop[c[1]]
        total += 4
        if i1 == "D" or i2 == "D":       # "DD", "DH", "HD", "DR", "RD"
            pheno += 4                   # all cases result in dominant allele
        elif i1 == "H" and i2 == "H":    # "HH"
            pheno += 3                   # not dominant if both happen do be recessive
        elif i1 == "H" and i2 == "R":    # "HR"
            pheno += 2                   # dominant if H happens to be dominant
        elif i1 == "R" and i2 == "H":    # "RH"
            pheno += 2                   # same
        else:                            # "RR"
            pass                         # never dominant
    print(pheno/total)

#solution("sample1.txt")
solution("dataset1.txt")
