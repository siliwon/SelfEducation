n = int(input())
a = n // 1000
b = n // 100 % 10
c = n % 100 // 10
d = n % 1000 % 100 % 10
print(1 if (a == d and b == c) else 2)
