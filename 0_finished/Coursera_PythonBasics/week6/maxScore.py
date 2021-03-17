class Man:
    name = ''
    lastname = ''
    class_type = 0
    score = 0


list = []
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        elements = []
        for i in line.split():
            elements.append(i)
        man = Man()
        man.name = elements[0]
        man.lastname = elements[1]
        man.class_type = int(elements[2])
        man.score = (elements[3])
        list.append(man)
        elements.clear()


def max_score(list, number):
    local_list = []
    for i in list:
        if i.class_type == number:
            local_list.append(i.score)
    if local_list == []:
        return 0
    return max(local_list)


with open('output.txt', 'w', encoding='utf8') as file:
    print(max_score(list, 9), max_score(list, 10),
          max_score(list, 11), file=file)
