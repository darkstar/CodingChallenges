def readfasta(ifile):
    dna = {}
    with open(ifile, mode="r") as f:
        id = None
        s = ""
        for l in f.readlines():
            if l[0] == ">":
                if id:
                    dna[id] = s
                id = l.strip()[1:]
                s = ""
            else:
                s = s + l.strip()
        dna[id] = s
    return len(s), dna
    
def solution(ifile):
    l, dna = readfasta(ifile)
    profile = { 'A': [0] * l, 'C': [0] * l, 'G': [0] * l, 'T': [0] * l }

    # build profile matrix
    for x in dna.values():
        for i in range(len(x)):
            profile[x[i]][i] += 1

    # build consensus string
    consensus = ""
    for i in range(l):
        pos = dict(zip("ACGT", map(lambda x: x[i], profile.values())))
        best = max(pos, key=pos.get)
        consensus += best

    print(consensus)
    for c in "ACGT":
        print("{}:".format(c), *profile[c])

#solution("sample1.txt")
solution("dataset1.txt")
