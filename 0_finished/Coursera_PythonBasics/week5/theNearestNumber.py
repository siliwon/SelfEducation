n = int(input())
list = list(map(int, input().split()))
x = int(input())
number = list[0]
for i in list:
    if abs(x - i) < abs(x - number):
        number = i
print(number)
