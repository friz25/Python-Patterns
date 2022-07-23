"""Поведенческий

Снимок (Memento) - позволяет сохранять и восстанавливать прошлое состояние обьектов
(не раскрывая подробности их реализации)
[+] не нарушает инкапсуляцию обьекта
[+] упрощает его структуру
[-] затраты памяти (выделяемой при частом создании снимка состояния)"""
#Пример. Система анализа работы биржи
import abc
from typing import Deque

class IMemento(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_dollars(self) -> int:
        pass

    @abc.abstractmethod
    def get_euro(self) -> int:
        pass

class ExchangeMemento(IMemento):
    """ Снимок состояния биржи """
    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self) -> int:
        return self.__dollars

    def get_euro(self) -> int:
        return self.__euro

class Exchange:
    """ Биржа """
    def __init__(self, d: int, e: int):
        self.__dollars = d
        self.__euro = e

    def get_dollars(self):
        print(f'Кол-во Долларов на бирже: {self.__dollars}')

    def get_euro(self):
        print(f'Кол-во Евро на бирже: {self.__euro}')

    def sell(self):
        """ чтоб продавать доллары """
        if self.__dollars > 0:
            self.__dollars -= 1

    def buy(self):
        """ чтоб покупать евро """
        self.__euro += 1

    def save(self) -> ExchangeMemento:
        """ делает снимок состояния Биржи """
        return ExchangeMemento(self.__dollars, self.__euro)

    def restore(self, exchange_memento: IMemento):
        """ по переданному в него снимку - будет восстанавливать значение долларов и евро"""
        self.__dollars = exchange_memento.get_dollars()
        self.__euro = exchange_memento.get_euro()

class Memory:
    """ Класс для хранения состояний/снимков """
    def __init__(self, exchange: Exchange):
        self.__exchange = exchange
        self.__history: Deque[IMemento] = [] # память со снимками

    def backup(self):
        """ будет записывать в память снимок (вызванный при помощи exchange())"""
        self.__history.append(self.__exchange.save())

    def undo(self):
        if len(self.__history) == 0:
            return
        else:
            self.__exchange.restore(self.__history.pop())

if __name__ == '__main__':
    exchange = Exchange(d=10, e=10) # создали Биржу

    memory = Memory(exchange) # добавили биржу в менеджер хранения снимков

    #отобразим текущее состояние нашей биржи
    exchange.get_dollars()
    exchange.get_euro()

    print('---- Продажа доллара, покупка евро ----')
    exchange.sell()
    exchange.buy()

    # отобразим текущее состояние нашей биржи
    exchange.get_dollars()
    exchange.get_euro()

    print('---- Сохранение состояния -------------')
    memory.backup()

    print('---- Продажа доллара, покупка евро ----')
    exchange.sell()
    exchange.buy()

    # отобразим текущее состояние нашей биржи
    exchange.get_dollars()
    exchange.get_euro()

    print('---- Восттановление состояния ---------')
    memory.undo()

    # отобразим текущее состояние нашей биржи
    exchange.get_dollars()
    exchange.get_euro()
"""
Кол-во Долларов на бирже: 10
Кол-во Евро на бирже: 10
---- Продажа доллара, покупка евро ----
Кол-во Долларов на бирже: 9
Кол-во Евро на бирже: 11
---- Сохранение состояния -------------
---- Продажа доллара, покупка евро ----
Кол-во Долларов на бирже: 8
Кол-во Евро на бирже: 12
---- Восттановление состояния ---------
Кол-во Долларов на бирже: 9
Кол-во Евро на бирже: 11

"""