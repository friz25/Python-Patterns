"""Структурный

Фасад (Facade) - позволяет скрыть сложность системы путём сведения всех (возможных внешних) вызовов
 к одному обьекту (делегирующему их соответствующим обьектам системы)

Фасад - применяеться для установки некоего рода политики по отношению к другой группе обьектов"""
# Пример - Работа МаркетПлейса и его составных подразделений
class ProvicerCommunication:
    """ Отдел по приёму товаров (от производителей) """
    def receive(self):
        print('Получение продукции от производителя')

    def payment(self):
        print('Оплата поставщику (за товар) с удержанием комисси за продажу продукции')

class Site:
    """ Отдел ИТ (по сопровождению сайта компании)"""
    def placement(self):
        print('Размещение на сайте')

    def delete(self):
        print('Удаление с сайта')

class Database:
    def insert(self):
        print('Добавление товара в БД')

    def delete(self):
        print('Удаление товара из БД')

class MarketPlace:
    def __init__(self):
        self._provicer_communication = ProvicerCommunication()
        self._site = Site()
        self._database = Database()

    def product_receipt(self):
        """ в случае поступления товара """
        self._provicer_communication.receive()
        self._site.placement()
        self._database.insert()

    def product_release(self):
        """ в случае реализации товара"""
        self._provicer_communication.payment()
        self._site.delete()
        self._database.delete()

if __name__ == '__main__':
    market_place = MarketPlace()
    market_place.product_receipt()
    print()
    market_place.product_release()
"""
Получение продукции от производителя
Размещение на сайте
Добавление товара в БД

Оплата поставщику (за товар) с удержанием комисси за продажу продукции
Удаление с сайта
Удаление товара из БД
"""
