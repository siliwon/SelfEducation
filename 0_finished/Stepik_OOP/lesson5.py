try:
    1 / 0
except ZeroDivisionError as err:
    print('Zero division error')
except (KeyError, IndexError):
    print('Lookup error')

# s = "hello"
# d = {}
#
# try:
#     i = 0
#     while True:
#         print(i)
#         i += 1
# except:
#     print("error")

# def second():
#     print('start second')
#     1 / 0
#     print('finish second')
#
#
# def first():
#     print('start first')
#     second()
#     print('finish first')
#
# print('hello')
# try:
#     first()
# except ZeroDivisionError:
#     print('handling')