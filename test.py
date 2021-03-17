first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 7, 6, 10, 2, 3, 6, 6, 2]

my_dict = dict()

for i in first_list:
    if i not in my_dict.keys():
        my_dict[i] = 1
    else:
        my_dict[i] += 1

for key, value in my_dict.items():
    if my_dict[key] == max(my_dict.values()):
        print(key)


my_string = 'asdlfkjsdfsasasdaf3pqo12312iwuerAAAAAwlkrt'
lst = []
for i in my_string:
    if i not in lst:
        lst.append(i)
new_string = ''.join(lst)
print(new_string)
