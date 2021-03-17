n = int(input())
i = 1
j = 1
my_sum = 1
while n != 0:
    n1 = int(input())
    if n1 == 0:
        break
    elif n1 > n:
        i += 1
        n = n1
        j = 1
        if i > my_sum:
            my_sum = i
    elif n1 < n:
        j += 1
        n = n1
        i = 1
        if j > my_sum:
            my_sum = j
    else:
        i = 1
        j = 1
        continue
print(my_sum)
