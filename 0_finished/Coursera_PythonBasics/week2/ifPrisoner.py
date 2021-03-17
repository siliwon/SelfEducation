a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

max_hole = max(d, e)
min_hole = min(d, e)

max_stone = max(a, b, c)
min_stone = min(a, b, c)
middle_stone = a + b + c - max_stone - min_stone

if min_hole >= min_stone:
    if max_hole >= max_stone:
        print('YES')
    elif max_hole >= middle_stone:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
