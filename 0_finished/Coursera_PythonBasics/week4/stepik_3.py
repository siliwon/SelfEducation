n = int(input())
my_list = []
i = 1
while i <= n:
    my_list.append(int(input()))
    i += 1

dictionary = {}
for i in my_list:
    if i not in dictionary:
        dictionary.update({i: f(i)})

for i in my_list:
    print(dictionary[i])
