"""Поведенческий

Команда (Command) - обьект используеться для инкапсуляции всей информации нужной для выполнения/вызова обьекта (в будущем)"""
#Пример. Пульт управления Конвеером
import abc
from typing import List, Deque

class ICommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def positive(self):
        pass
    @abc.abstractmethod
    def negative(self):
        pass

class Conveyor:
    def on(self):
        print('Конвейер запущен')

    def off(self):
        print('Конвейер остановлен')

    def speed_increase(self):
        print('Увеличена скорость конвеера')

    def speed_decrease(self):
        print('Снижена скорость конвеера')

class ConveyorWorkCommand(ICommand):
    """ Класс управления работой конвеера """
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.on()

    def negative(self):
        self.conveyor.off()

class ConveyorAdjustCommand(ICommand):
    """ Класс регулировки конвеера """
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.speed_increase()

    def negative(self):
        self.conveyor.speed_decrease()

class Multipult:
    """ Класс управления конвеером """
    def __init__(self):
        self.__commands: List[ICommand] = [None, None] # Список различных комманд
        self.__history: Deque[ICommand] = []           # История комманд

    def set_command(self, button: int, command: ICommand):
        """ устанавливаем в список комманд (__commands) - конкретную команду по индексу кнопки"""
        self.__commands[button] = command

    def press_on(self, button: int):
        """ вызовет positive() метод из списка (по указанному индексу)
        (и) запишет в историю комманд - выполненную комманду"""
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def press_cancel(self):
        """ извлечёт из истории комманд последнюю записанную
         (и) выполнит её отпицательный метод"""
        if len(self.__history) != 0:
            self.__history.pop().negative()

if __name__ == '__main__':
    conveyor = Conveyor() # создали конвеер

    multipult = Multipult() # создали пульт управления (конвеером)
    multipult.set_command(0, ConveyorWorkCommand(conveyor)) # установим в 0 адресс (списка комманд) - экземпляр класса Работы конвеера
    multipult.set_command(1, ConveyorAdjustCommand(conveyor))# установим в 1 адресс (списка комманд) - экземпляр класса Регулировки работы конвеера

    multipult.press_on(0)
    multipult.press_on(1)
    multipult.press_cancel()
    multipult.press_cancel()
"""
Конвейер запущен
Увеличена скорость конвеера
Снижена скорость конвеера
Конвейер остановлен
"""


