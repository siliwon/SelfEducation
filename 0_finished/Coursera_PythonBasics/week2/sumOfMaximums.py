my_list = []
n = int(input())
while n != 0:
    my_list.append(n)
    n = int(input())
print(my_list.count(max(my_list)))
