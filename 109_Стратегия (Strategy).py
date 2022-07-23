"""Поведенческий

Стратегия (Strategy) - он определяет семейство схожих алгоритмов (помещает каждый из них в собственный класс)
[+] паттерн изолирует код алгоритмов от остальных классов
[+] алгоритмы можно быстро заменять во время работы проги"""
#Пример. Система парсинга новостей с различных инфо-ресурсов (применяя к каждому из них свою стратегию парсинга)
import abc

class Parser(metaclass=abc.ABCMeta):
    """ Абстрактный парсер """
    @abc.abstractmethod
    def parse(self, url: str):
        pass

class ResourceParser:
    def __init__(self, parser: Parser):
        self.__parser = parser

    def set_strategy(self, parser: Parser):
        """ чтоб изменять парсер на другой """
        self.__parser = parser
        
    def parse(self, url: str):
        """ парсит (выбранным назначенным set_strategy() парсером)"""
        self.__parser.parse(url)
        
class NewsSiteParser(Parser):
    def parse(self, url: str):
        print('Парсинг новостного сайта:', url)
        
class SocialNetworkParser(Parser):
    def parse(self, url: str):
        print('Парсинг ленты новостей социальной сети:', url)

class TelegramChannelParser(Parser):
    def parse(self, url: str):
        print('Парсинг канала мессенджера Telegram:', url)

if __name__ == '__main__':
    resource_parser = ResourceParser(NewsSiteParser())

    url = 'https://news.com'
    resource_parser.parse(url)

    url = 'https://www.facebook.com/groups/1278692272467147'
    resource_parser.set_strategy(SocialNetworkParser())
    resource_parser.parse(url)

    url = '@news_channel_telegram'
    resource_parser.set_strategy(TelegramChannelParser())
    resource_parser.parse(url)
"""
Парсинг новостного сайта: https://news.com
Парсинг ленты новостей социальной сети: https://www.facebook.com/groups/1278692272467147
Парсинг канала мессенджера Telegram: @news_channel_telegram
"""