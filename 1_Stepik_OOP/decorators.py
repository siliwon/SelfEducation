
#
# def main_function(value):
#     name = value
#     def inner_function():
#         print('hello', name)
#
#     return inner_function

def adder(value):
    def inner(a):
        return a + value

    return inner