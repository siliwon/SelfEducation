x, y = float(input()), float(input())


def is_point_in_square(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


if is_point_in_square(x, y):
    print('YES')
else:
    print('NO')
