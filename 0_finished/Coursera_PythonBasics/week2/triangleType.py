x, y, z = int(input()), int(input()), int(input())
c = max(x, y, z)
a = min(x, y, z)
b = x + y + z - c - a

if a >= (b + c) or b >= (a + c) or c >= (a + b):
    print('impossible')
elif c ** 2 == a ** 2 + b ** 2:
    print('rectangular')
elif c ** 2 > a ** 2 + b ** 2:
    print('obtuse')
else:
    print('acute')
