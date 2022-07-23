"""Поведенческий

Наблюдатель (Observer) - позволяет одним обьектам наблюдать (и реагировать на события) (происходящие в других обьектах)"""
#Пример. Система наблюдения за ценой товара (Покупателем и Оптовым покупателем)
import abc
from typing import List

class IObserver(metaclass=abc.ABCMeta):
    """ Абстрактный наблюдатель """
    @abc.abstractmethod
    def update(self, p: int):
        pass

class IObservable(metaclass=abc.ABCMeta):
    """ Абстрактный наблюдаемый обьект """
    @abc.abstractmethod
    def add_observer(self, o: IObserver):
        """ добавление наблюдателя """
        pass

    @abc.abstractmethod
    def remove_observer(self, o: IObserver):
        """ удаление наблюдателя """
        pass

    @abc.abstractmethod
    def notify(self):
        pass

class Product(IObservable):
    def __init__(self, price: int):
        self.__price = price  # цена
        self.__observers: List[IObserver] = [] # список наблюдателей (за товаром)

    def change_price(self, price: int):
        self.__price = price
        self.notify()

    def add_observer(self, o: IObserver):
        self.__observers.append(o)

    def remove_observer(self, o: IObserver):
        self.__observers.remove(o)

    def notify(self):
        """ сообщит наблюдателям - об изменении стоимости товара """
        for o in self.__observers:
            o.update(self.__price)

class Wholesale(IObserver):
    """ Оптовик """
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self) # я буду наблюдать за (переданным в меня) товаром

    def update(self, p: int):
        if p < 300:
            print(f'Оптовик закупил товар по цене {p}')
            self.__product.remove_observer(self) # удаляемся из списка наблюдателей

class Buyer(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 350:
            print(f'Покупатель закупил товар по цене {p}')
            self.__product.remove_observer(self)

if __name__ == '__main__':
    product = Product(400) # создали продукт

    wholesale = Wholesale(product) # создали Оптовика
    buyer = Buyer(product)   # создали Покупателя

    product.change_price(320)
    product.change_price(280)
    """
    Покупатель закупил товар по цене 320
    Оптовик закупил товар по цене 280
    """

