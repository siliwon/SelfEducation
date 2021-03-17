number = int(input())
c = number % 100 % 10
a = number // 100
b = number // 10 % 10
print(a + b + c)
