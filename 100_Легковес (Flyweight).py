"""Структурный

Легковес (Flyweight) - позволяет вместить большее количество обьектов (в отведённую оперативную память)
[+] Легковес экономит память, выделяя и сохраняя общие параметры объектов.
[-] расходуеться процессорное время (на поиск)
[-] изза введения доп классов (усложняеться код проги)"""
# Пример. Учёт ИТшников разных компаний (приехавших на IT конфренцию)
from typing import List
from typing import Dict

class Shared:
    """(повторящиеся) Общие свойства представителя компании (название компании, должность)"""
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position

class Unique:
    """ (уникальные) свойства участников (Имя, Паспорт) """
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__password = passport

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password

class Flyweight:
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print(f'Отображаем новые данные: общие - {self.__shared.company}_{self.__shared.position} и уникальные {unique.name}_{unique.password}')

    def get_data(self) -> str:
        return self.__shared.company + '_' + self.__shared.position

class FlyweightFactory:
    """ Здесь будук храниться и накапливаться общие данные представителей компаний"""
    def get_key(self, shared: Shared):
        """ создаёт ключ словаря (содержащего общие свойства участников конференции)"""
        return f'{shared.company}_{shared.position}'

    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_flyweight(self, shared: Shared):
        """ чтоб получать легковесы (из их таблицы) по ключу (созданному на основании общих свойств)"""
        key: str = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            print(f'Фабрика легковесов: Общий обьект по ключу {key} не найден. Создаем новый.')
            self.__flyweights[key] = Flyweight(shared)
        else:
            print(f'Фабрика легковесов: Извлекаем данные из имеющихся записей по ключу {key}.')
        return self.__flyweights[key]

    def list_flyweights(self):
        """ выводит в консоль (количество записей в словаре) и (эти записи)"""
        count: int = len(self.__flyweights)
        print(f'\nФабрика легковесов: Всего {count} записей.')
        for pair in self.__flyweights.values():
            print(pair.get_data())

def add_specialist_database(ff: FlyweightFactory, company: str, position: str, name: str, passport: str):
    """ Добавляет Спец-а (участника конференции) """
    print()
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))

if __name__ == '__main__':
    shared_list: List[Shared] = \
        (Shared("Microsoft", "Управляющий"),
         Shared("Google", "Android-разработчик"),
         Shared("Google", "Web-разработчик"),
         Shared("Apple", "IPhone-разработчик"),
         )
    factory = FlyweightFactory(shared_list)
    factory.list_flyweights() # Фабрика легковесов: Всего 4 записей. ...

    add_specialist_database(factory, "Google", "Web-разработчик", "Борис", "AM-17234332")
    add_specialist_database(factory, "Apple", "Управляющий", "Александр", "DE-2211032")

    factory.list_flyweights() # Фабрика легковесов: Всего 5 записей. ...
"""
Фабрика легковесов: Всего 4 записей.
Microsoft_Управляющий
Google_Android-разработчик
Google_Web-разработчик
Apple_IPhone-разработчик

Фабрика легковесов: Извлекаем данные из имеющихся записей по ключу Google_Web-разработчик.
Отображаем новые данные: общие - Google_Web-разработчик и уникальные Борис_AM-17234332

Фабрика легковесов: Общий обьект по ключу Apple_Управляющий не найден. Создаем новый.
Отображаем новые данные: общие - Apple_Управляющий и уникальные Александр_DE-2211032

Фабрика легковесов: Всего 5 записей.
Microsoft_Управляющий
Google_Android-разработчик
Google_Web-разработчик
Apple_IPhone-разработчик
Apple_Управляющий
"""