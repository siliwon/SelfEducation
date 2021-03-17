s = input()
first_h = s.find('h')
second_h = s.rfind('h')
new_s = s[:first_h + 1] + s[first_h + 1:second_h] * 2 \
        + s[second_h:]
print(new_s)
