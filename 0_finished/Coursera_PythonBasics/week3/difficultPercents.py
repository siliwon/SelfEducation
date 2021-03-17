p, x, y = int(input()), int(input()), int(input())
k = int(input())

bank = x * 100 + y
for i in range(k):
    bank += int(bank * p / 100)
print(int(bank // 100), int(bank % 100))
