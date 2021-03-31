class Vector:

    def __init__(self, *args):
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)

    def __str__(self):
        if len(self.values) == 0:
            return f"Пустой вектор"
        return f"Вектор("  + ', '.join(map(str, sorted(self.values))) + ")"


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"