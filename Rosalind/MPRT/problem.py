import requests
import re

def readfasta(uniprot_id):
    fasta = requests.get("https://rest.uniprot.org/uniprotkb/{}.fasta".format(uniprot_id))
    if fasta.status_code != 200:
        print("Error reading UNIPROT sequence {}".format(uniprot_id))
        exit(1)
    fasta = fasta.text.split('\n')
    id = fasta[0][1:]
    seq = "".join(fasta[1:])
    return id, seq

def solution(ifile):
    with open(ifile, mode="r") as f:
        for l in [x.strip() for x in f.readlines()]:
            _, seq = readfasta(l.split("_")[0])
            offsets = []
            for i in range(len(seq)):
                if re.match(r'N[^P][ST][^P]', seq[i:]):
                    offsets += [i + 1]
            if len(offsets) > 0:
                print(l)
                print(*offsets)

#solution("sample1.txt")
solution("dataset1.txt")
