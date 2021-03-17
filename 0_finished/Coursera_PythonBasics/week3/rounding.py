from math import ceil, floor


x = float(input())
if (x - int(x)) * 10 >= 5:
    print(ceil(x))
else:
    print(floor(x))
