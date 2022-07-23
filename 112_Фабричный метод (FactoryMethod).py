"""Пораждающий паттерн

Фабричный метод (FactoryMethod) - предоставляет дочерним классам интерфейс для создания экземпляров какогото класса
(тоесть делигирует создание обьектов наследниками родительского класса)
[+] позволяет оперировать не классами а абстракциями
[+] позволяет установить связь между паралельными иерархиями классов
[-] нужно создавать наследника (для каждого нового типа)
"""
#Пример. Создание авто (легк и груз)
class IProduct:
    """ абстрактный выпускаемый продукт """
    def release(self):
        pass

class Car(IProduct):
    def release(self):
        print('Выпущен новый легковой автомобиль')

class Truck(IProduct):
    def release(self):
        print('Выпущен новый ГРУЗОВОЙ автомобиль')

class IWorkShop:
    """ абстрактный цех по производству авто """
    def create(self) -> IProduct:
        pass

class CarWorkshop(IWorkShop):
    def create(self) -> IProduct:
        return Car()

class TruckWorkshop(IWorkShop):
    def create(self) -> IProduct:
        return Truck()

if __name__ == '__main__':
    creator = CarWorkshop() # создали цех по созданию авто
    car = creator.create()

    creator = TruckWorkshop() # создали цех по созданию грузовиков
    truck = creator.create()

    car.release()
    truck.release()
"""
Выпущен новый легковой автомобиль
Выпущен новый ГРУЗОВОЙ автомобиль
"""

