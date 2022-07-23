"""SOLID
4)ISP - Interface Segregation Principle - Принцип разделения интерфейса
Программные сущности не должны зависеть от методов (которые они не используют)
(Много интерфейсов под конкретного юзера)"""
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionalPrinter(Machine): #когда реализуете комбайн - всё норм
    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass

class OldFashionedPrinter(Machine): # ОШИБКА
    def print(self, document):
        # OK
        pass

    def fax(self, document):
        pass #no code

    def scan(self, document):
        """ Not supported! """
        #no code / или можно:
        raise NotImplementedError('Printer cannot scan!')

""" Решение """
class Printer:
    @abstractmethod
    def print(self, document):
        raise NotImplementedError

class Scanner:
    @abstractmethod
    def scan(self, document):
        raise NotImplementedError

class OldFashionedPrinter2(Printer): #Вот так правильно
    def print(self, document):
        # code
        pass

class PrinterScanner(Printer, Scanner):
    def print(self, document):
        # code
        pass
    def scan(self, document):
        # code
        pass

class MultiFunctionalDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionalDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
