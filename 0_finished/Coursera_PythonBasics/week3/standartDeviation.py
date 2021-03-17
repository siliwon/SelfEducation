import math

x = int(input())
my_sum = 0
squared_sum = 0
n = 1
while x != 0:
    squared_sum += x ** 2
    my_sum += x
    x = int(input())
    if x == 0:
        break
    else:
        n += 1


print(math.sqrt((squared_sum - (my_sum ** 2) / n) / (n - 1)

                ))
