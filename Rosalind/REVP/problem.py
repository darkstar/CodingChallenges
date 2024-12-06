codons = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "-", "UAG": "-", "UGU": "C", "UGC": "C", "UGA": "-", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

comp = { "A": "T", "T": "A", "G": "C", "C": "G" }

def readfasta(ifile):
    seq = ""
    id = ""
    with open(ifile, mode="r") as f:
        s = ""
        for l in f.readlines():
            if l[0] == ">":
                id = l.strip()[1:]
            else:
                s = s + l.strip()
        seq = s
    return id, seq

def revcomp(seq):
    return "".join(map(lambda x: comp[x], seq[::-1]))

def solution(ifile):
    _, seq = readfasta(ifile)
    for l in range(4, 13):
        for i in range(0, len(seq) - l + 1):
            sub = seq[i:i+l]
            if sub == revcomp(sub):
                print("{} {}".format(i + 1, l, sub))

#solution("sample1.txt")
solution("dataset1.txt")
