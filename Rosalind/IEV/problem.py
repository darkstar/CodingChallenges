#       AA-AA AA-Aa AA-aa Aa-Aa Aa-aa aa-aa
prob = [  1.0,  1.0,  1.0, 0.75,  0.5,   0 ]

def solution(ifile):
    with open(ifile, mode="r") as f:
        s = list(map(int, f.readline().strip().split(" ")))

    offspring = list(map(lambda x, y: 2 * x * y, s, prob))
    print(sum(offspring))

#solution("sample1.txt")
solution("dataset1.txt")
