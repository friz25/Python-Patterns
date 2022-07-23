"""Структурный

Мост - разделяет абстракцию и реализацию так, чтобы они могли изменяться независимо
(для реализации Моста -  применили абстракции IDataReader и Sender)"""
import abc

class IDataReader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

class DatabaseReader(IDataReader):
    def read(self):
        print('Данные из БД: ', end='')

class FileReader(IDataReader):
    def read(self):
        print('Данные из Файла: ', end='')

class Sender(metaclass=abc.ABCMeta):
    def __init__(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    def set_data_reader(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    @abc.abstractmethod
    def send(self):
        pass

class EmailSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправлены при помощи Email')

class TelegramBotSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправлены при помощи Telegram бота')

if __name__ == '__main__':
    sender: Sender = EmailSender(DatabaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()

    sender = TelegramBotSender(DatabaseReader())
    sender.send()
"""
Данные из БД: отправлены при помощи Email
Данные из Файла: отправлены при помощи Email
Данные из БД: отправлены при помощи Telegram бота
"""