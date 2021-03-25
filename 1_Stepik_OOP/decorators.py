#
# def main_function(value):
#     name = value
#     def inner_function():
#         print('hello', name)
#
#     return inner_function
# def adder(value):
#     def inner(a):
#         return a + value
#
#     return inner
# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
# def average_numbers():
#     sum = 0
#     length = 0
#     def inner(number):
#         nonlocal sum
#         nonlocal length
#         sum += number
#         length += 1
#         return sum / length
#     return inner
# from time import perf_counter
#
#
# def timer():
#     start = perf_counter()
#
#     def inner():
#         return perf_counter() - start
#
#     return inner
# def add(a, b):
#     return a + b
#
#
# def counter(func):
#     count = 0
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"Функция {func.__name__} вызывалась {count} раз")
#         return func(*args, **kwargs)
#
#     return inner
from functools import wraps

def header(func):
    @wraps
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print("</table>")
    return inner


@table
@header
def say(name):
    print(f'hello, {name}!')



def  sqr(x):
    """
    powers argument in second degree
    :param x:
    :return:
    """
    print(x ** 2)



say('me')

# say = table(header(say))
# say('you')