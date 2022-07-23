"""SOLID
2)OCP - Open Closed Principle - Принцип открытости-закрытости
(Классы (всегда) открыты - для расширения, закрыты - для изменения)"""

"""Wep App Супермаркет"""
# from enum import Enum
#
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#
# class Size(Enum):
#     SMALL = 1
#     MEDIUM = 2
#     LARGE = 3
#
# class Product:
#     def __init__(self, name, color, size):
#         self.name = name
#         self.color = color
#         self.size = size
#     """одно из требований - фильтрация продуктов (по цвету)"""
# class ProductFilter:
#     def filter_by_color(self, products, color):
#         for p in products:
#             if p.color == color: yield p
#
#     def filter_by_size(self, products, size): #добавлением этого метода - нарушили принцип ОткрытостиЗакрытости
#         for p in products:
#             if p.size == size: yield p
#
#     def filter_by_size_and_color(self, products, size, color):
#         for p in products:
#             if p.color == color and p.size == size:
#                 yield p
#     """тоесть всего для 2х критериев 3 метода (2 --> 3)"""
#     """ (3 --> 7) !Ошибка = это не масштабируеться"""
#
# """Решение: Реализуем Specification"""
# class Specification:
#     def is_satisfied(self, item):
#         pass
#
#     def __and__(self, other): # (Улучшили 2)
#         return AndSpecification(self, other)
#
# class Filter:
#     def filter(self, items, spec): #spec - это любая(ые) спецификация (цвет, размер, цена, ...)
#         pass
# """Теперь мы не будем их менять их только расширять"""
# class ColorSpecification(Specification):
#     def __init__(self, color):
#         self.color = color
#
#     def is_satisfied(self, item):
#         return item.color == self.color
#
# class SizeSpecification(Specification):
#     def __init__(self, size):
#         self.size = size
#
#     def is_satisfied(self, item):
#         return item.size == self.size
#
# class AndSpecification(Specification): # (Улучшили 1)
#     def __init__(self, *args):
#         self.args = args
#     def is_satisfied(self, item):
#         return all(map(
#             lambda spec: spec.is_satisfied(item), self.args
#         ))
#
# """Пример Конкретная реализация Filter (который может чтото находить)"""
# class BetterFilter(Filter):
#     def filter(self, items, spec):
#         for item in items:
#             if spec.is_satisfied(item):
#                 yield item
#
# if __name__ == '__main__':
#     apple = Product('Apple', Color.GREEN, Size.SMALL)
#     tree = Product('Tree', Color.GREEN, Size.LARGE)
#     house = Product('House', Color.BLUE, Size.LARGE)
#
#     products = [apple, tree, house]
#
#     pf = ProductFilter()
#     print('Green products (old):')
#     for p in pf.filter_by_color(products, Color.GREEN):
#         print(f' - {p.name} is green')
#     """
#     Green products (old):
#      - Apple is green
#      - Tree is green
#     """
#     bf = BetterFilter()
#     print('Green products (new):')
#     green = ColorSpecification(Color.GREEN)
#     for p in bf.filter(products, green):
#         print(f' - {p.name} is green')
#     """
#     Green products (new):
#      - Apple is green
#      - Tree is green
#     """
#     print('Large products')
#     large = SizeSpecification(Size.LARGE)
#     for p in bf.filter(products, large):
#         print(f' - {p.name} is large')
#     """
#     Large products
#      - Tree is large
#      - House is large
#     """
#     # НА ЭТОМ ЭТАПЕ ОНИ ДАЮТ ОДИНАКОВЫЕ РЕЗУЛЬТАТЫ (Тогда где выгода? Когда МиксуемПоиск)
#     print('Large blue items:')
#     # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
#     large_blue = large & ColorSpecification(Color.BLUE) # уменьшили
#     for p in bf.filter(products, large_blue):
#         print(f' - {p.name} is large and blue')
#     """
#     Large blue items:
#      - House is large and blue
#     """
from enum import Enum

class Color(Enum):
    GREEN = 1
    RED = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size

class ISpec:
    def is_satisfied(self, item: Product) -> bool:
        pass

    def __and__(self, other):
        return AndSpec(self, other)

class IFilter:
    def filter(self, items, spec: ISpec):
        pass

class ColorSpec(ISpec):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color

class SizeSpec(ISpec):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size

class AndSpec(ISpec):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class Filter(IFilter):
    def filter(self, items, spec: ISpec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = Filter()
    print('Green products (new):')
    green = ColorSpec(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('Large products')
    large = SizeSpec(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('Large blue items:')
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large & ColorSpec(Color.BLUE) # уменьшили
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')