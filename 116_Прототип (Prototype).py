"""Порождающий паттерн

Прототип (Prototype) - позволяет копировать обьекты (не вдаваясь в подробности их реализации)
[+] уменьшает повторяющийся код при инициализации обьектов
[-] сложнее копировать составные обьекты (имеющие ссылки на другие обьекты)"""
#Пример. Клонирование овечки Долли
import copy

class Sheep:
    __name: str = ''
    __params: dict = {'Вес': 20, 'Рост': .34}

    def __init__(self, donor: 'Sheep' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_params(self) -> dict:
        return self.__params

    def set_weight(self, new_weight: int):
        self.__params['Вес'] = new_weight

    def clone(self):
        return Sheep(self)

if __name__ == '__main__':
    sheep_donor: Sheep = Sheep()
    sheep_donor.set_name('Долли')

    sheep_clone: Sheep = sheep_donor.clone()

    # отобразим (имена, параметры) созданных овечек
    print('Донор:', sheep_donor.get_name(), sheep_donor.get_params())
    print('Клон:', sheep_clone.get_name(), sheep_clone.get_params())


    # ИЗМЕНИМ (имена, параметры) копии  [этот паттерн он про это]
    sheep_clone.set_weight(35)
    sheep_clone.set_name('Новая Долли')
    print()

    print('Донор:', sheep_donor.get_name(), sheep_donor.get_params())
    print('Клон:', sheep_clone.get_name(), sheep_clone.get_params())
"""
Донор: Долли {'Вес': 20, 'Рост': 0.34}
Клон: Долли {'Вес': 20, 'Рост': 0.34}

Донор: Долли {'Вес': 20, 'Рост': 0.34}
Клон: Новая Долли {'Вес': 35, 'Рост': 0.34}
"""