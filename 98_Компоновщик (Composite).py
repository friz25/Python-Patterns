"""Структурный

Компоновщик - обьединяет объекты в древовидную структуру для представления иерархии
(Компоновщик - позволяет клиентам обращаться к отдельным обьектам и к группам обьектов одинаково)"""
#Пример. Выпадающее меню
import abc

class Item(metaclass=abc.ABCMeta):
    """ Абстрактный элемент пункта меню """
    def __init__(self, name: str):
        self._item_name: str = name # название текущего элемента
        self._owner_name: str = None # имя элемента (в который он вложен)

    def set_owner(self, o: str):
        """ устанавливаем имя владельца текущего элемента """
        self._owner_name = o

    @abc.abstractmethod
    def add(self, sub_item: 'Item'):
        pass

    @abc.abstractmethod
    def remove(self, sub_item: 'Item'):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class ClickableItem(Item):
    """ Кликабельный элемент меню """
    def __init__(self, name: str):
        super().__init__(name)

    def add(self, sub_item: Item):
        raise Exception('Кликабельному элементу нельзя добавить подэлемент')

    def remove(self, sub_item: Item):
        raise Exception('У кликабельного элемента не могут быть подэлементы')

    def display(self):
        print(self._owner_name + self._item_name)

class DropDownItem(Item):
    """ Выпадающий пункт меню """
    def __init__(self, name: str):
        super().__init__(name)
        self.__children = []

    def add(self, sub_item: Item):
        sub_item.set_owner(self._item_name)
        self.__children.append(sub_item)

    def remove(self, sub_item: Item):
        self.__children.remove(sub_item)

    def display(self):
        for item in self.__children:
            if self._owner_name is not None:
                print(self._owner_name, end='')
            item.display()

if __name__ == '__main__':
    file: Item = DropDownItem('файл->')

    create: Item = DropDownItem('Создать->')
    open_: Item = DropDownItem('Открыть->')
    exit_: Item = DropDownItem('Выход')

    file.add(create)
    file.add(open_)
    file.add(exit_)

    project: Item = ClickableItem('Проект...')
    repository: Item = ClickableItem('Репозиторий...')

    create.add(project)
    create.add(repository)

    solution: Item = ClickableItem('Решение...')
    folder = ClickableItem('Папка...')

    open_.add(solution)
    open_.add(folder)

    file.display()
    print()

    file.remove(create)
    file.display()
"""
файл->Создать->Проект...
файл->Создать->Репозиторий...
файл->Открыть->Решение...
файл->Открыть->Папка...

файл->Открыть->Решение...
файл->Открыть->Папка...
"""


