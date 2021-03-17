s = input()
first_h = s.find('h')
second_h = s.rfind('h')
new_s = s[:first_h] + s[second_h + 1:]
print(new_s)
