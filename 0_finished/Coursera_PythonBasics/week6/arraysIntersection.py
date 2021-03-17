list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list = []
list.extend(list_a)
list.extend(list_b)
list.sort()
i = 1
while i < len(list):
    if list[i] == list[i - 1]:
        print(list[i], end=' ')
        i += 2
    else:
        i += 1
