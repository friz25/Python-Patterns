"""Поведенческий

Шаблонный метод (Template method) - определяющий основу алгоритма
(и позволяющий наследникам переобределять некоторые шаги алгоритма (не изменяя его структуру вцелом))
[+] облегчает повторное использование кода"""
#Пример. Передатчик речи (может быть аналоговым и цифровым)
import abc

class Transmitter(metaclass=abc.ABCMeta):
    def _voice_record(self):
        print('Запись фрагмента речи')

    def _simpling(self):
        """ Дескритизация речи """
        pass

    def _digitization(self):
        """ Оцифровка речи """
        pass

    @abc.abstractmethod
    def _modulation(self):
        """ Модуляция в радио-сигналы """
        pass

    def _transmission(self):
        print('Передача сигнала по радиоканалу')

    def process_start(self):
        self._voice_record()
        self._simpling()
        self._digitization()
        self._modulation()
        self._transmission()

class AnalogTransmitter(Transmitter):
    def _modulation(self):
        print('Модуляция аналогового сигнала')

class DigitalTransmitter(Transmitter):
    def _simpling(self):
        print('Дискретизация записанного фрагмента')

    def _digitization(self):
        print('Оцифровка')

    def _modulation(self):
        print('Модуляция ЦИФРОВОГО сигнала')

if __name__ == '__main__':
    analog_transmitter = AnalogTransmitter()
    analog_transmitter.process_start()

    print()

    digital_transmitter = DigitalTransmitter()
    digital_transmitter.process_start()
"""
Запись фрагмента речи
Модуляция аналогового сигнала
Передача сигнала по радиоканалу

Запись фрагмента речи
Дискретизация записанного фрагмента
Оцифровка
Модуляция ЦИФРОВОГО сигнала
Передача сигнала по радиоканалу

"""
