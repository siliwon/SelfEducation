class Vector:

    def __init__(self, *args):
        values = []
        for arg in args:
            if isinstance(arg, int):
                values.append(arg)
        self.values = sorted(values)

    def __str__(self):
        if len(self.values) == 0:
            return f"Пустой вектор"
        return f"Вектор{tuple(self.values)}"

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*map(lambda x: x[0] + x[1], zip(self.values, other.values)))
            print("Сложение векторов разной длины недопустимо")
        elif isinstance(other, int):
            return Vector(*map(lambda x: x + other, self.values))
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*map(lambda x: x[0] * x[1], zip(self.values, other.values)))
            else:
                print("Умножение векторов разной длины недопустимо")
        if isinstance(other, int):
            return Vector(*map(lambda x: x * other, self.values))
        else:
            print(f"Вектор нельзя умножать с {other}")

    def __rmul__(self, other):
        return self + other

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"

v5 + 'hi' # печатает "Вектор нельзя сложить с hi"


v1 = Vector()
print(v1)
print(v1.values)







#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             if len(self.values) == len(other.values):
#                 self.values = tuple(map(lambda x: x[0] + x[1], zip(self.values, other.values)))
#                 return self
#             return "Сложение векторов разной длины недопустимо"
#         if isinstance(other, (int)):
#             self.values = [*map(lambda x: x + other, self.values)]
#             return self
#         return f"Вектор нельзя сложить с {other}"
#
#     def __radd__(self, other):
#         return other.__add__(self)
#
#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             if len(self.values) == len(other.values):
#                 self.values = [*map(lambda x: x[0] * x[1], zip(self.values, other.values))]
#                 return self
#             return "Умножение векторов разной длины недопустимо"
#         if isinstance(other, (int)):
#             self.values = [*map(lambda x: x * other, self.values)]
#             return self
#         return f"Вектор нельзя умножать с {other}"
#
#     def __rmul__(self, other):
#         return self * other
#
# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
#
# print(v1)
# print(v2)
# v3 = v1 + v2
# v4 = v2 + v1
# print(v3)
# print(v4)
# print(v3.values)
# print(v4.values)
# v5 = v1 + v2
# print(v5)
