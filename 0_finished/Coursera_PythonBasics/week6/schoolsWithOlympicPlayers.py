table = []
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        elements = []
        for i in line.split():
            elements.append(i)
        table.append(int(elements[-2]))
        elements.clear()

count_list = {}
table.sort()
for i in table:
    if i not in count_list.keys():
        count_list.update({i: table.count(i)})
with open('output.txt', 'w', encoding='utf8') as file:
    for key, value in count_list.items():
        if value == max(count_list.values()):
            print(key, end=' ', file=file)
