n = int(input())


def phib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return phib(n - 1) + phib(n - 2)


print(phib(n))
