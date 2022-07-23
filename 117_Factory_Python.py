"""Пораждающий паттерн

Фабричный метод (FactoryMethod) - предоставляет дочерним классам интерфейс для создания экземпляров какогото класса"""
#Пример. Пиццерия
from enum import Enum

class PizzaType(Enum):
    MARGARITA = 0,
    MEXICO = 1.
    STELLA = 2

class IPizza:
    """ Абстрактная пицца """
    def __init__(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price

class PizzaMargarita(IPizza):
    def __init__(self):
        super().__init__(3.5)
class PizzaMexico(IPizza):
    def __init__(self):
        super().__init__(17.5)
class PizzaStella(IPizza):
    def __init__(self):
        super().__init__(35.5)

def create_pizza(pizza_type: PizzaType) -> IPizza:
    """ Factory method """
    factory_dict={
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.STELLA: PizzaStella
    }
    return factory_dict[pizza_type]()

if __name__ == '__main__':
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')
"""
Pizza type: PizzaType.MARGARITA, price: 3.5
Pizza type: PizzaType.MEXICO, price: 17.5
Pizza type: PizzaType.STELLA, price: 35.5
"""