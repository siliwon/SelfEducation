list = list(map(int, input().split()))
minimum = []
for i in list:
    if i > 0:
        minimum.append(i)
print(min(minimum))
