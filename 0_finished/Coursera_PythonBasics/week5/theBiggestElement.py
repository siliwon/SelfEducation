list = list(map(int, input().split()))
maximum = max(list)
index = list.index(maximum)
print(maximum, index, sep=' ')
