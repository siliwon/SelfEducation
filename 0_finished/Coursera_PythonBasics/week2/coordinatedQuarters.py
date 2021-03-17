x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())


def quarter(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3


a = quarter(x1, y1)
b = quarter(x2, y2)
print('YES') if a == b else print('NO')
