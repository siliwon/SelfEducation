clients = dict()


def deposit(dict: dict, name, sum):
    dict[name] = dict.get(name, 0) + sum
    return dict


def withdraw(dict: dict, name, sum):
    dict[name] = dict.get(name, 0) - sum
    return dict


def balance(dict: dict, name):
    print(dict[name]) if name in dict.keys() \
        else print('ERROR')


def transfer(dict: dict, name1, name2, sum):
    withdraw(dict, name1, sum)
    deposit(dict, name2, sum)


def income(dict: dict, percent):
    for key, value in dict.items():
        if value > 0:
            dict[key] = int(value * percent / 100) + value
    return dict


def operation(list: list):
    if list[0] == 'deposit':
        deposit(clients, list[1], list[2])
    elif list[0] == 'withdraw':
        withdraw(clients, list[1], list[2])
    elif list[0] == 'balance':
        balance(clients, list[1])
    elif list[0] == 'transfer':
        transfer(clients, list[1], list[2], list[3])
    elif list[0] == 'income':
        income(clients, list[1])


with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip().lower()
        command = []
        for i in line.split():
            if i.isdigit():
                command.append(int(i))
            command.append(i)
        operation(command)
