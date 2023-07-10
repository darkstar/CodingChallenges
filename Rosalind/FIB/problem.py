import functools

@functools.cache
def fib(n, k):
    if n <= 2:
        return 1
    return fib(n - 1, k) + k * fib(n - 2, k)

def solution(ifile):
    with open(ifile, mode="r") as f:
        n, k = map(int, f.readline().split(" "))

    print(fib(n, k))

#solution("sample1.txt")
solution("dataset1.txt")
