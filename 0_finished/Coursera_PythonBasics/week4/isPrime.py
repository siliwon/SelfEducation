from math import sqrt

x = int(input())


def min_divisor(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return 'NO'
    return 'YES'

print(min_divisor(x))
