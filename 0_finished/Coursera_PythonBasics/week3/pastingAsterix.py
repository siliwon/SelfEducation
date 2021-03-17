string = input()
for i in string[:-1]:
    print(i, '*', sep='', end='')
print(string[-1])
