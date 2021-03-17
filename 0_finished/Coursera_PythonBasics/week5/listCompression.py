list = list(map(int, input().split()))
number_list = []
zero_list = []
for i in list:
    if i == 0:
        zero_list.append(i)
    else:
        number_list.append(i)
print(*number_list + zero_list)
