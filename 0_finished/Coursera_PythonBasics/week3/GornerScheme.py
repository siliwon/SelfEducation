n = float(input())
x = float(input())
i = 1
my_sum = 0
while i <= n:
    a = float(input())
    my_sum += a * (x ** n)
    n -= i
a = float(input())
my_sum += a
print(my_sum)
