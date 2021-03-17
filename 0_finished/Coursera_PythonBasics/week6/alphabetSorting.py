list = []
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        list.append(line.split())
counter = 0
new_list = []


def list_summary(list):
    return [list[0], list[1], int(list[3])]


for i in list:
    new_list.append(list_summary(i))
new_list.sort()
with open('output.txt', 'w', encoding='utf8') as file:
    for i in new_list:
        for j in i:
            print(j, end=' ', file=file)
        print('', file=file)
