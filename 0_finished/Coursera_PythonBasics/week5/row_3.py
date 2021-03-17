n = int(input())

number = 10 ** n
end = 10 ** (n - 1)

for i in range(number - 1, end - 1, -2):
    print(i, end=' ')
