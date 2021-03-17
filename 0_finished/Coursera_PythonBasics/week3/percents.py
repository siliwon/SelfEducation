p, x, y = int(input()), int(input()), int(input())

bank = x * 100 + y
percents = bank * p / 100
bank += percents
print(int(bank // 100), int(bank % 100))
