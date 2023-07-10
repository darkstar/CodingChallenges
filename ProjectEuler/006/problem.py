import math

def sum_of_squares(n):
    return (n * (2 * n + 1) * (n + 1)) // 6

def square_of_sum(n):
    x = n * (n + 1) // 2
    return x * x

print(abs(sum_of_squares(100) - square_of_sum(100)))
