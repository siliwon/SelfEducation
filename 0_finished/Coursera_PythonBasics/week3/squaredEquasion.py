a, b, c = float(input()), float(input()), float(input())
x1, x2 = 0, 0
D = b ** 2 - (4 * a * c)
if D > 0:
    x1 = (- b + D ** 0.5) / (2 * a)
    x2 = (- b - D ** 0.5) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep=' ')
elif D == 0:
    x1 = (-b) / (2 * a)
    print(x1)
