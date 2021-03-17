a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
max1 = max(a1, b1, c1)
min1 = min(a1, b1, c1)
middle1 = a1 + b1 + c1 - max1 - min1
max2 = max(a2, b2, c2)
min2 = min(a2, b2, c2)
middle2 = a2 + b2 + c2 - max2 - min2
if max1 == max2 and middle1 == middle2 and min1 == min2:
    print('Boxes are equal')
elif max1 <= max2 and middle1 <= middle2 and min1 <= min2:
    print('The first box is smaller than the second one')
elif max1 >= max2 and middle1 >= middle2 and min1 >= min2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
