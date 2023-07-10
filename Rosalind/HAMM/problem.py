import operator

def hamming(s1, s2):
    return len(list(filter(lambda x: x, (map(operator.ne, s1, s2)))))

def solution(ifile):
    with open(ifile, mode="r") as f:
        s1, s2 = f.readlines()

    print(hamming(s1.strip(), s2.strip()))

#solution("sample1.txt")
solution("dataset1.txt")
