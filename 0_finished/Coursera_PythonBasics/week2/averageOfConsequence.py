n = int(input())
my_sum = n
i = 1
while n != 0:
    n = int(input())
    if n != 0:
        my_sum += n
        i += 1
print(my_sum / i)
