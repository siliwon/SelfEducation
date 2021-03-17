list = list(map(int, input().split()))
increase = 0
for i in range(1, len(list)):
    if list[i] > list[i - 1]:
        increase += 1
    else:
        increase = 0
if increase == len(list) - 1:
    print('YES')
else:
    print('NO')
