a = float(input())
n = float(input())


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


print(power(a, n))
