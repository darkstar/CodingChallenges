# array indices: aa=0, Aa=1, AA=2
#      A:
#      0  1  2
#B: 0  .  .  .
#   1  .  .  .
#   2  .  .  .
#

def solution(ifile):
    with open(ifile, mode="r") as f:
        s = [int(x) for x in f.readline().strip().split()]

    # we start with Tom
    alleles = { "AbBb": 1 }

    for gen in range(s[0]):
        newalleles = {}
        for k, v in alleles.items():
            # merge the offspring
            offspring(v, k, "AaBb", newalleles)
        print("after gen {}: {}".format(gen, newalleles))
        alleles = newalleles

solution("sample1.txt")
#solution("dataset1.txt")
