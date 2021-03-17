n = int(input())
k = int(input())


def c(n, k):
    if k == n:
        return 1
    elif k == 1:
        return n
    elif k == 0 or n == 0:
        return 1
    return c(n - 1, k) + c(n - 1, k - 1)


print(c(n, k))
