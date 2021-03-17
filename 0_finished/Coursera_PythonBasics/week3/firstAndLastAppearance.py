string = input()
i = 0
a = string.find('f')
b = string.rfind('f')
if a != -1 and b != -1:
    if a == b:
        print(a)
    else:
        print(a, b)
