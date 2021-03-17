list = list(map(int, input().split()))
k = int(input())

for i in range(0, len(list)):
    if i == k:
        continue
    print(list[i], end=' ')
