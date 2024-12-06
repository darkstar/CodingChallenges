import itertools

def solution(ifile):
    with open(ifile, mode="r") as f:
        n = int(f.readline().strip())
    l = list(itertools.permutations(range(1, n+1)))
    print(len(l))
    for i in l:
        print(" ".join(map(str, i)))

#solution("sample1.txt")
solution("dataset1.txt")

