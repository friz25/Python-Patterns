"""SOLID
5)DIP - Принцип инверсии зависимостей / Dependency Inversion Principle
Модули верхнего уровня не должны зависеть от модулей нижнего уровня
(добавляем абстракций!)"""
from abc import abstractmethod
from enum import Enum

"""Будем определять отношения между 2мя людьми"""
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser: # добавили (Абстракция прослойка)
    @abstractmethod
    def find_all_children_of(self, name): pass

class Relationships(RelationshipBrowser): # low-level module
    """Класс в котором будух храниться все отношения"""
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )
    def find_all_children_of(self, name): # добавили реализацию абстрактной прослойки
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research: # high-level module

    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:                                         # перенесли в class Relationships
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT: # перенесли в class Relationships
    #             print(f'John has a child {r[2].name}.')             # перенесли в class Relationships

    def __init__(self, browser: Relationships):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}.')

parent = Person('John')
child1 = Person('Chriss')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
"""
John has a child Chriss.
John has a child Matt.
"""
"""Если мы изменим хранилище (class Relationships) то это повлияет на (class Research) = не будет работать """
"""Так что добавим прослойку абстракцию (class RelationshipBrowser)"""