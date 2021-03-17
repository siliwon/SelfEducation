list = list(map(int, input().split()))
my_set = set()
for i in list:
    if i not in my_set:
        print('NO')
        my_set.add(i)
    else:
        print('YES')
