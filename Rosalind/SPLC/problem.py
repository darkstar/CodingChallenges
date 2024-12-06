def readfasta(ifile):
    res = []
    with open(ifile, mode="r") as f:
        seq = ""
        id = None
        for l in f.readlines():
            if l[0] == ">":
                if id is not None:
                    res += [ (id, seq) ]
                id = l.strip()[1:]
                seq = ""
            else:
                seq = seq + l.strip()
        res += [ (id, seq) ]
    return res

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

def revcomp(seq):
    return "".join(map(lambda x: comp[x], seq[::-1]))

def transcribe(seq):
    res = ""
    while len(seq)>=3:
        a, b, c, *rest = seq
        aa = "".join([a, b, c]).replace("T", "U")
        res += codons[aa]
        seq = rest
    return res

def solution(ifile):
    (_, seq), *introns = readfasta(ifile)
    for _, i in introns:
        seq = seq.replace(i, "")

    # remember to drop the stop codon
    print(transcribe(seq)[:-1])

#solution("sample1.txt")
solution("dataset1.txt")
