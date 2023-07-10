def solution(ifile):
    with open(ifile, mode="r") as f:
        s = f.readline().strip()

    results = list(map(lambda x: s.count(x), "ACGT"))
    print(*results)

solution("sample1.txt")
#solution("dataset1.txt")
