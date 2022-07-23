"""Фабричный метод - это любой метод который создаёт обьект класса"""

"""Проблематика"""
"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    '''чтобы принимать (еще и) полярные координаты (как вариант)'''
    # def __init__(self, hto, theta): # НЕЛЬЗЯ(
    #     pass
"""
"""Решение"""
from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    """ получили плохой код
    (потому что - если нужно добавить еще одну систему координат) нужно будет:
     - изменить класс CoordinateSystem
     - добавить еще одну проверкуу внутри Point.__init__ (это нарушения принципа Открытости/Закрытости SOLID)
     а именно [классы всегда открыты - для расширения, закрыты - для изменения
     (также потому что)
     a, b - плохо, не понятно что это (в будущем) x,y (если декарт) и hto, theta (если Polar)"""
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * sin(b)
    #         self.y = a * cos(b)
    """ Решение - Фабричный метод"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y): #cartesian - декартовы координаты (x, y)
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p1, p2)
"""
x: 2, y: 3 x: -0.4161468365471424, y: 0.9092974268256817
"""