def inCircle(x, y, flag):
    # flag == True - нестрогое неравенство (включая границу окружности)
    # flag == False - строгое неравенство

    if flag:
        return (x + 1) ** 2 + (y - 1) ** 2 <= 4
    return (x + 1) ** 2 + (y - 1) ** 2 < 4


def inArea(x, y):
    # X + Y = 0
    # Y - 2X = 2
    return x + y >= 0 and y - 2 * x >= 2 and inCircle(x, y, True) \
           or x + y <= 0 and y - 2 * x <= 2 and not inCircle(x, y, False)


x, y = float(input()), float(input())

if inArea(x, y):
    print('YES')
else:
    print('NO')
