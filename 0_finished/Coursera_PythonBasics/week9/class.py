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


exec(stdin.read())
