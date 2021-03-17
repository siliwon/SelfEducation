class Man:
    name = ''
    lastname = ''
    class_number = 0
    score = 0


table = []
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        elements = []
        for i in line.split():
            elements.append(i)
        man = Man()
        man.name = elements[0]
        man.lastname = elements[1]
        man.class_number = int(elements[2])
        man.score = int(elements[3])
        table.append(man)
        elements.clear()


def structure_print(sturcture):
    for i in sturcture:
        print(i.name, end=' ')
        print(i.lastname, end=' ')
        print(i.class_number, end=' ')
        print(i.score)


def amount_of_winners(structure, number):
    list = []
    imax = 0
    for i in structure:
        if i.class_number == number:
            list.append(i.score)
    imax = max(list)
    return list.count(imax)


with open('output.txt', 'w', encoding='utf8') as file:
    print(amount_of_winners(table, 9),
          amount_of_winners(table, 10),
          amount_of_winners(table, 11), file=file)
