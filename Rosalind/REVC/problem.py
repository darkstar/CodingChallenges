translations = { "A": "T", "T": "A", "G": "C", "C": "G" }

def solution(ifile):
    with open(ifile, mode="r") as f:
        s = f.readline().strip()

    s = "".join(map(lambda x: translations[x], s[::-1]))
    print(s)

#solution("sample1.txt")
solution("dataset1.txt")
