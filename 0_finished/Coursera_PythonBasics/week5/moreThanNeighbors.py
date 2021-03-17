list = list(map(int, input().split()))
counter = 0
for i in range(1, len(list) - 1):
    if list[i] > list[i - 1] and \
            list[i] > list[i + 1]:
        counter += 1
print(counter)
