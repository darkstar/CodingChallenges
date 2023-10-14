import itertools

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
    num, seq = readfasta(ifile)

    seq = list(seq.values())

    s = seq[0]
    rest = seq[1:]

    for l in range(len(s) - 1, 1, -1):
        for i in range(0, len(s) - l + 1):
            sub = s[i:i+l]
            if all((sub in other) for other in rest):
                print(sub)
                return



#solution("sample1.txt")
solution("dataset1.txt")
