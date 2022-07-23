"""SOLID
3)LSP - Liskov Substitution Principle - Принцип подстановки Лисков
(Наследуемый класс должен дополнять/не замещать поведение родительского класса)"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @staticmethod
    def square(width, height): # ФАБРИЧНЫЙ МЕТОД (сам попробовал)
        return Rectangle(width, width)

class Square(Rectangle): # Нарушение принципа Liskov
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
use_it(rc) # Expected an area of 20, got 20

sq = Square(5)
use_it(sq) # ОШИБКА # Expected an area of 50, got 100
"""
Решение:
Класс Square - вообще не нужен
фабричный метод (который создаёт квадрат (вместо прямоугольника))
"""
sq2 = Rectangle.square(5,10) # ФАБРИЧНЫЙ МЕТОД (сам попробовал)
use_it(sq2) # Expected an area of 50, got 50

"""НИХУЯ НЕ ЯСНО (СКАЗАЛИ КАК НЕ НАДО ДЕЛАТЬ) (НЕ СКАЗАЛИ КАК НАДО)"""
"""предложили использовать фабричный метод (для решения этой проблемы)"""