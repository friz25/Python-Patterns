"""АДАПТЕР
совмещать классы которые не могут быть совместимыми"""
# JSON 100 cls, 100 intf
# XML
"""Для примера JSON - str, XMK - int"""

class Old:
    def get(self):
        return "1234"

class New:
    def get(self):
        return 456

class Adapter(New):
    def get(self):
        return str(super(Adapter, self).get())

def main(obj):
    print("Результат: "+obj.get())

if __name__ == '__main__':
    obj = Old() # работает (привык к JSON)
    obj = New() # Не работает (не привык к XML)
    obj = Adapter() # работает (XML приведён к JSON-формату) (атакже метод get_int() приведён к привычному get())
    main(obj)

