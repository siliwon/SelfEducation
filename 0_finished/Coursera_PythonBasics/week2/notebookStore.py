a, b, c = int(input()), int(input()), int(input())
x, y, z = int(input()), int(input()), int(input())

var1 = (a // x) * (b // y) * (c // z)
var2 = (a // y) * (b // z) * (c // x)
var3 = (a // z) * (b // x) * (c // y)
var4 = (a // x) * (b // z) * (c // y)
var5 = (a // y) * (b // x) * (c // z)
var6 = (a // z) * (b // y) * (c // x)
print(max(var1, var2, var3, var4, var5, var6))