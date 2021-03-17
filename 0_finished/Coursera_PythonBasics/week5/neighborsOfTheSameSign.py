list = list(map(int, input().split()))
for i in range(1, len(list)):
    if list[i] * list[i - 1] > 0:
        print(list[i - 1], list[i])
        break
    elif list[i - 1] == list[i] == 0:
        print(0, 0)
        break
