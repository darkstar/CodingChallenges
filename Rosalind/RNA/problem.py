def solution(ifile):
    with open(ifile, mode="r") as f:
        dna = f.readline().strip()

    print(dna.replace("T", "U"))

#solution("sample1.txt")
solution("dataset1.txt")
