import re

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

def to_rna(seq):
    return seq.replace("T", "U")

def translate(seq):
    s = ""
    for i in range(0, len(seq) // 3):
        cod = seq[3*i:3*i+3]
        s += codons[to_rna(cod)]
    return s

def solution(ifile):
    results = set()
    with open(ifile, mode="r") as f:
        fasta = [x.strip() for x in f.readlines()]
    seq = "".join(fasta[1:])

    l = len(seq)
    rseq = revcomp(seq)
    frames = [
            seq[:3*(l//3)],
            seq[1:1+3*((l-1)//3)],
            seq[2:2+3*((l-2)//3)],
            rseq[:3*(l//3)],
            rseq[1:1+3*((l-1)//3)],
            rseq[2:2+3*((l-2)//3)],
            ]
    for f in frames:
        prot = translate(f)
        for i in range(len(prot)-1):
            m = re.match(r'M[^-]*\-', prot[i:])
            if m:
                results.add(m.group(0)[:-1])
    for x in results:
        print(x)


#solution("sample1.txt")
solution("dataset1.txt")
