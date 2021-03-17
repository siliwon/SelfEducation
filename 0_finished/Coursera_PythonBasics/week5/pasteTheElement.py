list = list(map(int, input().split()))
k, C = map(int, input().split())
i = 0
while i < k:
    print(list[i], end=' ')
    i += 1
if i == k:
    print(C, end=' ')
while i < len(list):
    print(list[i], end=' ')
    i += 1
