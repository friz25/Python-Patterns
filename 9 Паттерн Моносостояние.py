"""
Паттерн Моносостояние - когда есть несколько Обьектов одного класса
(и если изменить переменную X в одном из них, чтобы она изменилась и в других) = синхронизация переменных
"""
class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs

if __name__ == '__main__':
    th1 = ThreadData()
    print(th1.__dict__)
    th2 = ThreadData()
    print(th2.__dict__)
"""
{'name': 'thread_1', 'data': {}, 'id': 1}
{'name': 'thread_1', 'data': {}, 'id': 1}
"""
