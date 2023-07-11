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
    n, seq = readfasta(ifile)

    for k1, v1 in seq.items():
        tail = v1[-3:]
        for k2, v2 in seq.items():
            # don't compare an element to itself
            if k1 == k2:
                continue

            head = v2[:3]

            if head == tail:
                print("{} {}".format(k1, k2))

#solution("sample1.txt")
solution("dataset1.txt")
