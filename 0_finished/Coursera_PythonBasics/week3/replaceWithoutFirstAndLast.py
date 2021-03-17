string = input()
a = string.find('h')
b = string.rfind('h')
new_string = string[:a + 1] + \
             string[a + 1:b].replace('h', 'H') + string[b:]
print(new_string)
