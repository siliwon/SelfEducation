def gcd(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    return gcd(b, a % b)


def ReduceFraction(n, m):
    l = gcd(n, m)
    return (n // l, m // l)


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
