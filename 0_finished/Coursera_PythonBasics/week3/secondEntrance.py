string = input()
new_string = string[string.find('f') + 1:]
if string.find('f') == -1:
    print(-2)
elif new_string.find('f') == -1:
    print(-1)
else:
    a = int(len(string[0:string.find('f') + 1]))
    b = int(len(new_string[0:new_string.find('f')]))
    print(a + b)
