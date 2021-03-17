height = int(input())
a = int(input())
b = int(input())
day = 1
day_distance = 0

while height > day_distance:
    day_distance += a
    if day_distance >= height:
        print(day)
    else:
        day_distance -= b
        day += 1
