k = int(input())
i = 1
my_sum = 0


def pallindrom(k):
    k1 = k % 100000 % 10000 % 1000 % 100 % 10
    k2 = k // 10 % 10000 % 1000 % 100 % 10
    k3 = k // 100 % 1000 % 100 % 10
    k4 = k // 1000 % 100 % 10
    k5 = k // 10000 % 10
    k6 = k // 100000
    if k1 == k:
        return True
    elif k2 * 10 + k1 == k:
        return True if k1 == k2 else False
    elif k3 * 100 + k2 * 10 + k1 == k:
        return True if k1 == k3 else False
    elif k4 * 1000 + k3 * 100 + k2 * 10 + k1 == k:
        return True if (k1 == k4 and
                        (k2 == k3)) else False
    elif k5 * 10000 + k4 * 1000 + k3 * 100 + k2 * 10 + k1 == k:
        return True if (k1 == k5 and
                        k2 == k3) else False
    elif k6 * 100000 + k5 * 10000 + k4 * 1000 + k3 * 100 + k2 * 10 + k1 == k:
        return True if (k1 == k6 and
                        k2 == k5 and k3 == k4) else False
    else:
        return False


while i <= k:
    if pallindrom(i):
        my_sum += 1
    i += 1
print(my_sum)
