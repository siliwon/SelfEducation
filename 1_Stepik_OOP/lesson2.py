class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should be a number')
        self.__balance = value

    def delete_balance(self):
        print('deleting balance')
        del self.__balance

    my_balance = property(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)


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
