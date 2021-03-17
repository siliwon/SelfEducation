list = list(map(int, input().split()))
high = int(input())
for i in list:
    if high > i:
        print(list.index(i) + 1)
        break
if high <= list[-1]:
    print(len(list) + 1)
