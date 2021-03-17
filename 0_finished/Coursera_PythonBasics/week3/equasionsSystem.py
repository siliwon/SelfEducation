a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
x, y = 0, 0

y = (f * a - c * e) / (a * d - c * b)
x = (e * d - b * f) / (a * d - b * c)

print(x, y, sep=' ')
