from math import sqrt

i = 1


def squares():
    global i
    n = int(input())
    if n != 0:
        squares()
        if n // sqrt(n) == sqrt(n):
            print(n, end=' ', sep=' ')
            i = 0


squares()
if i == 1:
    print(0)
