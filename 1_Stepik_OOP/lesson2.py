from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def if_includes_number(password):
        for d in digits:
            if d in password:
                return True
        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if len(value) < 4:
            raise ValueError('Password length is too small, '
                             'minimum 4 symbols required')
        if not User.if_includes_number(value):
            raise ValueError("Password must contain "
                             "at least one digit")
        print('setter called')
        self.__password = value


# class DepartmentIT:
#     PYTHON_DEV = 3
#     GO_DEV = 3
#     REACT_DEV = 2
#
#
#     def info(cls):
#         print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
#
#     def make_backend(self):
#         print('Python and go')
#
#     def make_frontend(self):
#         print("React")
#
#
# it1 = DepartmentIT()
# it1.info()
# class Example:
#
#     @staticmethod
#     def static_hello():
#         print('static hello')
#
#     @classmethod
#     def class_hello(cls):
#         print(f"class_hello, {cls}")
# class Sqr:
#
#     def __init__(self, s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area == None:
#             print('Calculating area')
#             self.__area = self.side ** 2
#         return self.__area
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def my_balance(self):
#         print('get balance')
#         return self.__balance
#
#     @my_balance.setter
#     def my_balance(self, value):
#         print('set balance')
#         if not isinstance(value, (int, float)):
#             raise ValueError('Balance should be a number')
#         self.__balance = value
#
#     @my_balance.deleter
#     def my_balance(self):
#         print('deleting balance')
#         del self.__balance
# class BankAccount:
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     # def print_public_data(self):
#     #     print(self.name, self.balance, self.passport)
#
#     # def print_protected_data(self):
#         # print(self._name, self._balance, self._passport)
#
#     def print_private_data(self):
#         print(self.__name, self.__balance, self.__passport)
#
# account1 = BankAccount('Bob', 100000, 456789123)
# account1.print_private_data()
# # print(account1.__name)
# # print(account1.__balance)
# # print(account1.__passport)
# print(dir(account1))
# class Cat:
#
#     def __init__(self, name, breed='pers', age=1, color='white'):
#         print('Hello! My new object is', self, name, breed, age, color)
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.color = color
# class Point:
#
#     list_points = []
#
#     def __init__(self, x=0, y=0):
#         self.move_to(x, y)
#         Point.list_points.append(self)
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.move_to(0, 0)
#
#     def print_point(self):
#         print(f"Точка с координатами ({self.x},{self.y})")
#
#     def calc_dist(self, other):
#         if not isinstance(other, Point):
#             raise ValueError("Аргумент должен принадлежать классу Точка")
#         return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
# class Cat:
#     __shared_attr = {
#         'breed': 'pers',
#         'color': 'black'
#     }
#
#     def __init__(self):
#         self.__dict__ = Cat.__shared_attr
