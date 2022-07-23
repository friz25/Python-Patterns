"""SOLID
1)SRP - Single Responsibility Principle - Принцип единственной ответственности
(1 Класс = 1 Задача)"""
"""
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')
'''
Journal entries:
1: I cried today.
2: I ate a bug.
'''
"""
"""Всё отлично работает, добавим классу обязанности которые он раньше не делал чтоб нарушить принцип"""
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save_to_file(self, filename):
    #     """сохранять журнал в файл"""
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     """загружать журнал из файла"""
    #     pass
    #
    # def load_from_web(self, uri):
    #     """загружать журнал по ссылке"""
    #     pass

class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

file = r'C:\PythonProjects\Python-Patterns-88\91-journal.txt'
PersistanceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())