import math

start1 = int(input())
start2 = int(input())
end1 = int(input())
end2 = int(input())


def king_sqr(a, b):
    return math.fabs(a - b)


if (king_sqr(end1, start1) <= 1) and (king_sqr(end2, start2) <= 1):
    print("YES")
else:
    print("NO")
