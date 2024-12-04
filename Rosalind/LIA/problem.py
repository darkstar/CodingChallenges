import math

def solution(ifile):
    with open(ifile, mode="r") as f:
        k, n = [int(x) for x in f.readline().strip().split()]

    # number of offspring in gen. k:
    total = 2**k

    # for x of the offspring to have alleles Aa Bb
    # chances are (n choose x) times 1/4^n (for the correct alleles)
    # times 3/4^n (for the incorrect alleles)
    probs = [ math.comb(total, x) * pow(1/4, x) * pow(3/4, total - x) for x in range(total + 1) ]

    # we only want the probabilities that *at least* N offspring have those alleles
    print(sum(probs[n:]))

#solution("sample1.txt")
solution("dataset1.txt")
