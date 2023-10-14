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
    with open(ifile, mode="r") as f:
        s = f.readline().strip()

    results = list(map(lambda x: s.count(x), "ACGT"))
    print(*results)

solution("sample1.txt")
#solution("dataset1.txt")
