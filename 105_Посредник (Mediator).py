"""Поведенческий

Посредник (Mediator) - позволяет уменьшить связанность множества классов между собой
(благодаря перемещению этих связей в один класс-посредник)"""
# Пример. Заказчик > Project Manager(Mediator) >> Designer >> Employee
import abc

class IMediator(metaclass=abc.ABCMeta): # Абстрактный Посредник
    @abc.abstractmethod
    def notify(self, emp: 'Employee', msg: str):
        pass

class Employee(metaclass=abc.ABCMeta): # Абстрактный работник организации
    def __init__(self, mediator: IMediator):
        self._mediator = mediator

    def set_mediator(self, med:IMediator):
        self._mediator = med

class Designer(Employee):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__is_working = False # работает ли в данный момент Дизайнер

    def execute_work(self):
        print('<-Дизайнер в работе')
        self._mediator.notify(self, 'Дизайнер проектирует...')

    def set_work(self, state: bool):
        """ устанавливает - состояние дизайнера (работает/не работает)"""
        self.__is_working = state
        if state:
            print('<-Дизайнер освобождён от работы')
        else:
            print('<-Дизайнер занят')

class Director(Employee):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__text: str = None # Приказы Директора

    def give_command(self, txt: str):
        self.__text = txt
        if txt == '':
            print('->Директор знает, что дизайнер уже работает')
        else:
            print('->Директор дал команду: ' + txt)
        self._mediator.notify(self, txt)

class ProjectManager(IMediator):
    def __init__(self, designer: Designer, director: Director):
        self.__designer = designer
        self.__director = director
        designer.set_mediator(self) # Назначаем этот класс - посредником (для них)
        director.set_mediator(self) # Назначаем этот класс - посредником (для них)

    def notify(self, emp: 'Employee', msg: str):
        if isinstance(emp, Director):
            if msg == '':
                self.__designer.set_work(False)
            else:
                self.__designer.set_work(True)

        if isinstance(emp, Designer):
            if msg == 'Дизайнер проектирует...':
                self.__director.give_command('')

if __name__ == '__main__':
    designer = Designer()
    director = Director()

    mediator = ProjectManager(designer, director)

    director.give_command('Проектировать')

    print()

    designer.execute_work()
"""
->Директор дал команду: Проектировать
<-Дизайнер освобождён от работы

<-Дизайнер в работе
->Директор знает, что дизайнер уже работает
<-Дизайнер занят
"""


