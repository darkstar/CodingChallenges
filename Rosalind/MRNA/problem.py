codons = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "-", "UAG": "-", "UGU": "C", "UGC": "C", "UGA": "-", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

rev_codons = { x: len([c for c in codons.keys() if codons[c] == x]) for x in codons.values() }

MODULUS = 1000000

def solution(ifile):
    with open(ifile, mode="r") as f:
        s = f.readline().strip()

    res = 1
    for c in s:
        res *= rev_codons[c]
    res *= rev_codons["-"]  # stop codon

    print(res % MODULUS)

#solution("sample1.txt")
solution("dataset1.txt")
