a, b, c = float(input()), float(input()), float(input())
d, e = float(input()), float(input())
counter = 0
for i in range(0, 1001):
    if i - e == 0:
        continue
    elif (a * (i ** 3) + b * (i ** 2) + c * i + d) / (i - e) == 0:
        counter += 1
print(counter)
