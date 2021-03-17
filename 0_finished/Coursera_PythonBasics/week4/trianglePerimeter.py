import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


perimeter = (abs(dist(x1, y1, x2, y2)) +
             abs(dist(x2, y2, x3, y3)) +
             abs(dist(x1, y1, x3, y3)))

print(perimeter)
