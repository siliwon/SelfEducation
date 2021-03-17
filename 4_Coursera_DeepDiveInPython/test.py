from datetime import date


class Human:

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def say_how_old(self):
        self._say(f"I am {self._age} years old")

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human._name}!")
        self.population.append(human)



# @Classmethod:
class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.event_date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.event_date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)


def extract_description(user_string):
    return "Открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)


class ComplexError(BaseException):
    def __init__(self, complex, other):
        self.first = complex
        self.second = other


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + '+' + str(self.im) + 'i'

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + other.re * self.im
            return Complex(re, im)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.re * other, self.im * other)
        else:
            error = ComplexError(self, other)
            raise error

    __rmul__ = __mul__


# a = Complex()
# b = Complex(1, 1)
# c = Complex(2, 3)
#
# try:
#     print('5' * b)
# except ComplexError as ce:
#     print(f'Multiplication Error, first param: {ce.first}, '
#           f'second param: {ce.second}!')

class Point(Complex):
    def length(self):
        return (self.re**2 + self.im**2) ** 0.5

    def __str__(self):
        return str((self.re, self.im))


class Robot:
    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print('make robot useless')
        del self._power

#
# wall_e = Robot(200)
# wall_e.power = -20
# print(wall_e.power)


class Pet:
    def __init__(self, name=None):
        self.name = name



class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f"{self.name}: waw!"


dog = Dog("Sharik", "Doberman")
print(dog.name)
print(dog.say())