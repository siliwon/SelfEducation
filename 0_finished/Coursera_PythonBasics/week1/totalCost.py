a = int(input())
b = int(input())
n = int(input())

cost = a * 100 + b
total_cost = cost * n

print(total_cost // 100, total_cost % 100)
