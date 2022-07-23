"""Прототип = использование copy.deepcopy()"""
class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'

john = Person('John', Address('123 London Road', 'London', 'UK'))
print(john) # John lives at 123 London Road, London, UK
""" Проблема: сделать Jane (живущую по тому же адресу)"""
jane = john
jane.name = 'Jane'
print("--------")
print(john) # ОШБИКА # Jane lives at 123 London Road, London, UK
print(jane) # Jane lives at 123 London Road, London, UK
"""еще попытка"""
address = Address('123 London Road', 'London', 'UK')
john = Person('John', address) # John lives at 123 London Road, London, UK
jane = Person('Jane', address) # Jane lives at 123 London Road, London, UK
print(john)
print(jane)
# но проблема (jane переехала)
jane.address.street_address = '399 London Road'
print(john) # ОШИБКА # John lives at 399 London Road, London, UK
print(jane) # Jane lives at 399 London Road, London, UK
"""решение copy.deepcopy()"""
import copy
john = Person('John', Address('123 London Road', 'London', 'UK'))
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = '399 London Road'
print(john) # John lives at 123 London Road, London, UK
print(jane) # Jane lives at 399 London Road, London, UK
