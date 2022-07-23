"""Поведенческий

Посетитель (Visitor) - позволяет добавлять в прогу новые операции (не изменяя классы обьектов (над которыми эти операции могут выполняться))
[+] обьединяет родственные операции в одном классе
[+] упрощает добавление операций (работающийх со сложными структурами обьектов)
[-] возможно нарушение инкапсуляции элементов"""
#Пример. Отдыхающий посещает различные места в городе))
import abc
from typing import List

class IVisitor(metaclass=abc.ABCMeta):
    """ Абстрактный посетитель """
    @abc.abstractmethod
    def visit(self, place: 'IPlace'):
        pass

class IPlace(metaclass=abc.ABCMeta):
    """ Абстрактное место """
    @abc.abstractmethod
    def accept(self, visitor: IVisitor):
        pass

class Zoo(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)

class Cinema(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)

class Circus(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)

class HolidayMaker(IVisitor):
    """ наш Отдыхающий"""
    def __init__(self):
        self.impressions = '' # то что посетитель видел при посещении того или иного места

    def visit(self, place: 'IPlace'):
        if isinstance(place, Zoo):
            self.impressions = 'Слон в зоопарке'
        elif isinstance(place, Cinema):
            self.impressions = 'Кино - Властелин колец'
        elif isinstance(place, Circus):
            self.impressions = 'Клоун в цирке'

if __name__ == '__main__':

    places: List[IPlace] = [Zoo(), Cinema(), Circus()] # список мест (которые желает посетить отдыхающий)

    for place in places:
        visitor = HolidayMaker() # создали посетителя
        place.accept(visitor) # посетитель смог посетить это место
        print(visitor.impressions) # вывод инфы об увиденном

"""
Слон в зоопарке
Кино - Властелин колец
Клоун в цирке
"""



