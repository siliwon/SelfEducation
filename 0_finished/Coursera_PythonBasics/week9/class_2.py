from sys import stdin


class Matrix:

    def __init__(self, list):
        self.list = [line.copy() for line in list]

    def __str__(self):
        return '\n'.join(map(lambda x: '\t'.join(map(str, x)), self.list))

    def size(self):
        row = len(self.list)
        column = len(self.list[0])
        return (row, column)

    def __add__(self, other):
        new = []
        for i in range(0, len(self.list)):
            new.append([])
            for j in range(0, len(self.list[i])):
                new[i].append(self.list[i][j] + other.list[i][j])
        return Matrix(new)

    def __mul__(self, other):
        new = []
        for i in range(0, len(self.list)):
            new.append([])
            for j in range(0, len(self.list[i])):
                new[i].append(self.list[i][j] * other)
        return Matrix(new)

    __rmul__ = __mul__


exec(stdin.read())
