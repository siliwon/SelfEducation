list = list(map(int, input().split()))
maximum = max(list)
if list.count(max(list)) > 1:
    new_list = []
    for i in range(len(list) - 1, -1, -1):
        new_list.append(list[i])
    print(maximum, len(list) - 1 - new_list.index(max(new_list)))
else:
    print(maximum, list.index(max(list)))
