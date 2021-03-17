contacts = []
check_number = ''


def number_transformation(number):
    if len(number) == 11:
        string = '8' + number[1:]
        return string
    else:
        string = '8495' + number
        return string


def check_the_phone_number(contacts, number):
    for i in contacts:
        if number == i:
            print('YES')
        else:
            print('NO')


with open('input.txt', 'r', encoding='utf8') as infile:
    for line in infile:
        line = line.strip()
        number = ''
        for i in line:
            if i.isdigit():
                number += i
        if check_number == '':
            check_number = number_transformation(number)
        else:
            contacts.append(number_transformation(number))
check_the_phone_number(contacts, check_number)
