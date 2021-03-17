n = int(input())


def sin(n):
    if n % 2 == 0:
        return 0
    elif n == 1:
        return 1
    elif n == (-1):
        return (-1)
    elif n > 0:
        return sin(n - 4)
    else:
        return sin(n + 4)


def sign(x):
    if n == 0:
        return 0
    elif n > 0:
        return 1
    else:
        return -1


print(sign(n))
