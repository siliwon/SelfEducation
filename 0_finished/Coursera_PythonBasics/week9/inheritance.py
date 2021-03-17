from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if self.size() != other.size():
            error = MatrixError(self, other)
            raise error
        else:
            new = []
            for i in range(0, len(self.list)):
                new.append([])
                for j in range(0, len(self.list[i])):
                    new[i].append(self.list[i][j] + other.list[i][j])
            return Matrix(new)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            arr = []
            for line in self.list:
                arr.append([*map(lambda x: x * other, line)])
            return Matrix(arr)
        elif isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            temp = Matrix.transposed(other)
            rows = self.size()[0]
            cols = temp.size()[0]
            arr = [[0 for _ in range(cols)] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    row_x_col = zip(self.list[row], temp.list[col])
                    arr[row][col] = sum(a * b for a, b in row_x_col)
            return Matrix(arr)
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        new = []
        for j in range(len(self.list[0])):
            lst = []
            for i in range(len(self.list)):
                lst.append(self.list[i][j])
            new.append(lst)
        self.list = new
        return Matrix(self.list)

    @staticmethod
    def transposed(self):
        new = []
        for j in range(len(self.list[0])):
            lst = []
            for i in range(len(self.list)):
                lst.append(self.list[i][j])
            new.append(lst)
        return Matrix(new)


class SquareMatrix(Matrix):
    def __pow__(self, m):
        new = []
        for i in self.list:
            lst = []
            for j in i:
                a = j ** m
                lst.append(a)
            new.append(lst)
        return SquareMatrix(new)

# exec(stdin.read())
# Task 6 check 3
m = SquareMatrix([[1, 1, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 0, 1]]
                )
print(m)
print('----------')
print(m ** 1)
print('----------')
print(m ** 2)
print('----------')
print(m ** 3)
print('----------')
print(m ** 4)
print('----------')
print(m ** 5)