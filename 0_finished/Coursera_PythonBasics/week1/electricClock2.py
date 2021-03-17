n = int(input())

hh = n // 3600 % 24
mm2 = n // 60 % 60 % 10
mm1 = n // 60 % 60 // 10
ss2 = n % 60 % 10
ss1 = n % 60 // 10

print(hh, ':', mm1, mm2, ':', ss1, ss2, sep='')
