class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        print('iter called')
        self.index = -1
        return self

    def __next__(self):
        return self.name[self.index]



igor = Student('Igor', 'Nicolaev', [3, 4, 4, 5, 4])

for i in igor:
    print(i)

# class Vector:
#
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return str(self.values)
#
#     def __getitem__(self, item):
#         if  0 <= item < len(self.values):
#             return self.values[item]
#         else:
#             raise IndexError("Index out of our collection range")
#
#     def __setitem__(self, key, value):
#         if 0 <= key < len(self.values):
#             self.values[key] = value
#         elif key > len(self.values):
#             diff = key - len(self.values)
#             self.values.extend([0] * diff)
#             self.values[key] = value
#         else:
#             raise IndexError('Index out of our collection range')
#
#     def __delitem__(self, key):
#         if 0 <= key < len(self.values):
#             del self.values[key]
#         else:
#             raise IndexError("Go fuck yourself, you're so stupid!")
#
#
# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_rect_area(self):
#         return self.a * self.b
#
#
# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def get_sqare_area(self):
#         return self.a ** 2
# from time import perf_counter
#

# class Timer:
#
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         print(f'a func called {self.fn.__name__}')
#         result = self.fn(*args, **kwargs)
#         finish = perf_counter()
#         print(f'The func worked {finish - start}')
#         return result
#
#
# def fact(n):
#     pr = 1
#     for i in range(1, n - 1):
#         pr *= i
#     return pr
#
#
# def fib(n):
#     if n < 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# class Counter:
#
#     def __init__(self):
#         self.counter = 0
#         self.sm = 0
#         self.amount = 0
#         print('init object', self)
#
#     def __call__(self, *args, **kwargs):
#         self.counter += 1
#         self.sm += sum(args)
#         self.amount += len(args)
#         print(f'our object {self} called {self.counter} times')
#
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __bool__(self):
#         print('bool called')
#         return self.x != 0 or self.y != 0
#
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
#     def __eq__(self, other):
#         print('equal called')
#         if isinstance(other, Rectangle):
#             return self.a == other.a and self.b == other.b
#
#     def __lt__(self, other):
#         print('less than called')
#         if isinstance(other, Rectangle):
#             return self.area < other.area
#         elif isinstance(other, (int, float)):
#             return self.area < other
#
#     def __le__(self, other):
#         return self == other or self < other
#
#
# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __repr__(self):
#         return f'Клиент {self.name} с балансом {self.balace}'
#
#     def __add__(self, other=0):
#         print('add called')
#         if isinstance(other, Bank):
#             return self.balance + other.balance
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         raise NotImplemented
#
#     def __radd__(self, other):
#         print('radd called')
#         return self + other
#
#
# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __len__(self):
#         return len(self.name + self.surname)
# class Lion:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"the object - {self.name}"
#
#     def __str__(self):
#         return f"lion {self.name}"