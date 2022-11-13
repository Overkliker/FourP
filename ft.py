import math


def reduce(x, y):
    k = math.gcd(x, y)
    return (x // k), (y // k)


x, y = int(input()), int(input())
print(reduce(x, y))
