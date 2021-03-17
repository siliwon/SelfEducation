a = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * power(a, n - 1)
    else:
        return power(a * a, n / 2)


print(power(a, n))
