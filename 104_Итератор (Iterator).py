"""Поведенческий

Iterator - это обьект, позволяющий получить последовательный доступ к элементам обьекта-агрегата"""
import abc
import copy


class DataStack:
    def __init__(self, my_stack: 'DataStack' = None):
        self.__item = [0] * 10 # массив содержащий 10 элементов
        self.__length = 0 # длинна данных записанных в стек

        if my_stack is not None:
            self.__items = copy.deepcopy(my_stack.__items)
            self.__length = my_stack.__length

    @property
    def items(self):
        return self.__items

    @property
    def length(self):
        return self.__length

    def push(self, value: int):
        """ чтоб добавлять элементы в массив items[] """
        self.__items[self.__length] = value
        self.__length += 1

    def pop(self) -> int:
        """ возвращает последний элемент массива items[] """
        self.__length -= 1
        return self.__items

    def __eq__(self, other: 'DataStack') -> bool:
        """ переопределили оператор сравнения """
        it1, it2 = StackIterator(self), StackIterator(other)

        while not it1.is_end() or not it2.is_end():
            if next(it1) != next(it2):
                break
        return it1.is_end() and it2.is_end()

class StackIterator:
    def __init__(self, my_stack: DataStack):
        self.__stack = my_stack
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_index = self.__index
        self.__index += 1
        if current_index < self.__stack.length:
            return self.__stack.items[current_index]
        return 0