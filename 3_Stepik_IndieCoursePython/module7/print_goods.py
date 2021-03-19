def print_goods(*args):
    lst = []
    for arg in args:
        if isinstance(arg, str) and arg != '':
            lst.append(arg)
    if len(lst) != 0:
        for i in lst:
            print(lst.index(i) + 1, i, sep='. ')
    else:
        print('Нет товаров')


print_goods([], {}, 1, 2)