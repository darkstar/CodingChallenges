def solution(ifile):
    with open(ifile, mode="r") as f:
        n, m = map(int, f.readline().strip().split(" "))

    rabbits = [1] + [0] * (m - 1)
    for _ in range(n - 1):
        rabbits = [sum(rabbits[1:])] + rabbits[:-1]

    print(sum(rabbits))


#solution("sample1.txt")
solution("dataset1.txt")
