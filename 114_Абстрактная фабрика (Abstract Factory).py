"""Порождающий паттерн

Абстрактная фабрика (Abstract Factory) - предоставляет интерфейс взаиосвязанных/взаимоЗависимых обьектов
- когда прога должна быть независима от процессов и типов новых создаваемых обьектов
- когда нужно создавать группы взаимосвязанных обьектов
[+] изолирует конкретные классы
[+] упрощает замену семейств продуктов
[+] гарантирует сочитаемость продуктов
[-] сложность добавления/поддержки нового вида продуктов"""
#Пример. Японская фабрика авто / Русская фабрика авто
from abc import ABCMeta, abstractmethod

class IEngine(metaclass=ABCMeta):
    """ абстрактный двигатель """
    @abstractmethod
    def release_engine(self):
        pass

class JapaneseEngine(IEngine):
    def release_engine(self):
        print('японский двигатель')

class RussianEngine(IEngine):
    def release_engine(self):
        print('русский двигатель')

class ICar(metaclass=ABCMeta):
    """ абстрактный выпускаемый автомобиль """
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass

class JapaneseCar(ICar):
    def release_car(self, engine: IEngine):
        print('Собрали японский автомобиль, ', end='')
        engine.release_engine()

class RussianCar(ICar):
    def release_car(self, engine: IEngine):
        print('Собрали РУССКИЙ автомобиль, ', end='')
        engine.release_engine()

class IFactory(metaclass=ABCMeta):
    """ абстрактная фабрика """
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass

class JapaneseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return JapaneseEngine()

    def create_car(self) -> ICar:
        return JapaneseCar()


class RussianFactory(IFactory):
    def create_engine(self) -> IEngine:
        return RussianEngine()

    def create_car(self) -> ICar:
        return RussianCar()

if __name__ == '__main__':
    j_factory = JapaneseFactory() # создали японскую фабрику
    j_engine = j_factory.create_engine()
    j_car = j_factory.create_car()

    j_car.release_car(j_engine)

    r_factory = RussianFactory()
    r_engine = r_factory.create_engine()
    r_car = r_factory.create_car()

    r_car.release_car(r_engine)
"""
Собрали японский автомобиль, японский двигатель
Собрали РУССКИЙ автомобиль, русский двигатель
"""





