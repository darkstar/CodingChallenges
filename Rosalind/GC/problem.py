def gc_content(s):
    return (s.count("G") + s.count("C")) / len(s)

def solution(ifile):
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

    gc = { k: gc_content(v) for k, v in dna.items() }
    best = max(gc, key = gc.get)
    print(best)
    print(100.0 * gc[best])

#solution("sample1.txt")
solution("dataset1.txt")
