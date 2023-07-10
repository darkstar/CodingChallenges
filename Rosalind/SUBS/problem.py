def solution(ifile):
    with open(ifile, mode="r") as f:
        s = f.readline().strip()
        t = f.readline().strip()

    pos = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            pos.append(i + 1)

    print(*pos)

#solution("sample1.txt")
solution("dataset1.txt")
