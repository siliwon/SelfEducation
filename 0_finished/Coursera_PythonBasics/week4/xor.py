x, y = float(input()), float(input())


def xor(x, y):
    if x == 1 and y == 0:
        return True
    elif x == 0 and y == 1:
        return True
    return False


print(int(xor(x, y)))
