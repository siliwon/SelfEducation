class NewInt(int):

    def repeat(self, number=2):
        string = str(self) * number
        return int(string)

    def to_bin(self):
        number = str(bin(self))
        return int(number[2:])


a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35
