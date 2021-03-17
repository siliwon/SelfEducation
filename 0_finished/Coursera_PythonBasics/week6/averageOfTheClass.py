class Man:
    name = ''
    lastname = ''
    class_number = 0
    score = 0


table = []
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
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


def average(table, number):
    counter = 0
    sum = 0
    for i in table:
        if i.class_number == number:
            sum += i.score
            counter += 1
    return sum / counter


with open('output.txt', 'w', encoding='utf8') as file:
    print(average(table, 9), average(table, 10), average(table, 11), file=file)
