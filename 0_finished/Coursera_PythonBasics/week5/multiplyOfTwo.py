list = list(map(int, input().split()))
min1 = min(list)
list.pop(list.index(min1))
min2 = min(list)
list.pop(list.index(min2))
max1 = max(list)
list.pop(list.index(max1))
max2 = max(list)
list.pop(list.index(max2))
if min1 * min2 > max1 * max2:
    print(min(min1, min2), max(min1, min2))
else:
    print(min(max1, max2), max(max1, max2))
