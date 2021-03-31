from lesson3 import Rectangle
from lesson3 import Square


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

square1 = Square(5)
square2 = Square(7)

print(rect1.get_rect_area(), end=' ')
print(rect2.get_rect_area())

print(square1.get_sqare_area(), end=' ')
print(square2.get_sqare_area())


figures = [rect1, rect2, square1, square2]
for figure in figures:
    print()