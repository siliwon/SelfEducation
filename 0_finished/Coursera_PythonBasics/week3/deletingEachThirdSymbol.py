string = input()
i = 0
while i < len(string):
    if i % 3 == 0:
        print('', sep='', end='')
        i += 1
    else:
        print(string[i], sep='', end='')
        i += 1
