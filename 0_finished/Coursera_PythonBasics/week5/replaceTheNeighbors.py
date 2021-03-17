list = list(map(int, input().split()))
new_list = []
last = []
if len(list) % 2 == 1:
    last.append(list[-1])
    list.pop(-1)
else:
    last = []
i = 1
while i <= len(list) - 1:
    new_list.append(list[i])
    new_list.append(list[i - 1])
    i += 2
if last == []:
    print(*new_list)
else:
    print(*(new_list + last))
