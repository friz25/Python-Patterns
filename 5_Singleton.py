# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("вызов __new__ для " + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("вызов __init__ для " + str(self))
#         self.x = x
#         self.y = y
#
# pt = Point(1, 2)
# print(pt)
"""
вызов __new__ для <class '__main__.Point'>
вызов __init__ для <__main__.Point object at 0x000002089CC87C40>
<__main__.Point object at 0x000002089CC87C40>
"""
"""Порождающий паттерн
(Отвечают за удобное и безопасное создание новых объектов( или даже целых семейств объектов))

SINDGLETON
смысл - в проге всегда может существовать только один экземпляр DataBase (или Логгирования)"""
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        """ выполняеться перед созданием обьекта (БД)
        *чтоб __new__() работал норм - в нём обязательно вконце должна быть строка
        return super().__new__(cls)
        (иначе __init__() ниже не выполнеться! --> и обьект DataBase вообще не будет создан!"""

        if cls.__instance is None: # если ранее уже создавался обьект DataBase -> новый создан не будет!!
            cls.__instance = super().__new__(cls)

        return cls.__instance # вместо этого мы просто вернём ссылку на ранее созданный обьект (и в __init__() "обновим все предыдущие")

    def __del__(self):
        DataBase.__instance = None
    """/\/\/\ эти строчки и определяют паттерн Singleton /\/\/\ """
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие соединение с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root222', '45645', 40)
# print(id(db), id(db2))

db.connect()
db2.connect()
"""
соединение с БД: root222, 45645, 40
соединение с БД: root222, 45645, 40
"""