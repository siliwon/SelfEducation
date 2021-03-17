my_list = []
n = int(input())
while n != 0:
    my_list.append(n)
    n = int(input())
my_list.pop(my_list.index(max(my_list)))
print(max(my_list))
