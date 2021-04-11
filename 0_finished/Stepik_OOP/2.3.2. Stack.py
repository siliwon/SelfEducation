class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if not self.is_empty():
            return self.values.pop()
        print('Empty Stack')
        return None

    def peek(self):
        if len(self.values) != 0:
            return self.values[-1]
        else:
            print('Empty Stack')
            return None
    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')
s.push('dog')
print(s.peek())  # распечатает 'dog'
s.push(True)
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2