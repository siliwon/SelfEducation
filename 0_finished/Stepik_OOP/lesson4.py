class Rectangle:

    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width= a
        self.height = b

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)

    @property
    def area(self):
        return self.height * self.width


# class PointSlots:
#
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Doctor:
#
#     def __init__(self, degree):
#         self.degree = degree
#
#     def graduate(self):
#         print('Horray, I have become a doctor!')
#
#
# class Builder:
#
#     def __init__(self, range):
#         self.range = range
#
#     def graduate(self):
#         print('And I have become a builder!')
#
#
# class Person(Doctor, Builder):
#
#     def __init__(self, range, degree, name):
#         Doctor.__init__(self,degree)
#         Builder.__init__(self, range)
#         self.name = name
#
#     def graduate(self):
#         print("Let's see who I've become!")
#         Doctor.graduate(self)
#         Builder.graduate(self)
#
#
# p = Person('phd', 2, 'Sam')
# print(p.degree, p.name, p.range)

# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
#     def breathe(self):
#         print('Person is breathing')
#
#
# class Doctor(Person):
#
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname)
#         self.age = age
#
#
#     def breathe(self):
#         print('Doctor is breathing')
#         super().breathe()
#
# p = Person('Ivan', 'Ivanov')
# print(p.name, p.surname)
# d = Doctor('Petr', 'Petrov', 44)
# print(d.name, d.surname, d.age)

# class Person:
#
#     NAME = 'Adam'
#
#     def breathe(self):
#         print("Person is breathing")
#
#     def walk(self):
#         print("Person is walking!")
#
#
# class Doctor(Person):
#
#     def breathe(self):
#         print("Doctor is breathing too")
#
#
# d = Doctor()
# d.breathe()
# p = Person()
# p.breathe()
# print(p.NAME)
# print(d.NAME)
#
#
# class Person:
#     def can_walk(self):
#         print('I can walk!')
#
#     def can_breathe(self):
#         print('I can breathe')
#
#
# class Doctor(Person):
#     def can_cure(self):
#         print('I can cure')
#
#
# class Architect(Person):
#     def can_build(self):
#         print('I can build')
#
#
# d = Doctor()
# a = Architect()
#
# print(issubclass(Person, object))
# print(isinstance(d, Person))
