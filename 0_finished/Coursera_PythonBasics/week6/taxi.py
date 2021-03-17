employees = list(map(int, input().split()))
fees = list(map(int, input().split()))

summary = 0
employees.sort(reverse=True)
fees.sort()

for i in range(len(employees)):
    summary += fees[i] * employees[i]

print(summary)
