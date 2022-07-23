"""Заместитель (Proxy) - вводим обьект (который контролирует доступ к другому обьекту) перехватывая все вызовы к нему
([+] в web app - снижаеться кол-во запросов к серверу (в нём применяеться КЕШИРОВАНИЕ ранее полученных данных)"""
# Пример. Работа Веб Браузера
import abc
from typing import Dict

class ISite(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_page(self, num: int) -> str:
        pass

class Site(ISite):

    def get_page(self, num: int) -> str:
        """ Возвращает абстрактную веб страницу (на основании её номера)"""
        return f'Это страница {num}'

class SiteProxy(ISite):
    def __init__(self, site: ISite):
        self.__site = site
        self.__cache: Dict[int, str] = {}

    def get_page(self, num: int) -> str:
        page: str = ''
        if self.__cache.get(num) is not None:
            page = self.__cache[num]
            page = 'из кеша: ' + page
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page
        return page

if __name__ == '__main__':
    my_site: ISite = SiteProxy(Site())

    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(3))

    print(my_site.get_page(2))
    """
    Это страница 1
    Это страница 2
    Это страница 3
    из кеша: Это страница 2
    """

