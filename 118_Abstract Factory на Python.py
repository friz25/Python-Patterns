"""Abstract Factory на Python"""
#Пример. GUI приложения (для Windows, Linux)
import abc
from abc import ABC, abstractmethod

""" Абстрактные классы GUI """

class IStatusBar(ABC):
    def __init__(self, system: str):
        self._system = system

    @abc.abstractmethod
    def create(self): pass

class IMainMenu(ABC):
    def __init__(self, system: str):
        self._system = system

    @abc.abstractmethod
    def create(self): pass

class IMainWindow(ABC):
    def __init__(self, system: str):
        self._system = system

    @abc.abstractmethod
    def create(self): pass

""" реализации абстрактных классов (которые выше) [для Windows]"""
class WindowsStatusBar(IStatusBar):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created status bar for {self._system}')


class WindowsMainMenu(IMainMenu):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created MAIN MENU for {self._system}')


class WindowsMainWindow(IMainWindow):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created main WINDOW for {self._system}')

""" реализации абстрактных классов (которые выше) [для Linux]"""
class LinuxStatusBar(IStatusBar):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created status bar for {self._system}')


class LinuxMainMenu(IMainMenu):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created MAIN MENU for {self._system}')


class LinuxMainWindow(IMainWindow):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created main WINDOW for {self._system}')

"""
абстрактная фабрика
"""

class GuiAbstractFactory(ABC):
    @abc.abstractmethod
    def getStatusBar(self) -> IStatusBar: pass

    @abc.abstractmethod
    def getMainMenu(self) -> IMainMenu: pass

    @abc.abstractmethod
    def getMainWindow(self) -> IMainWindow: pass

""" реализации абстрактной фабрики (для Windows, Linux)"""

class WindowsGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> IStatusBar:
        return WindowsStatusBar()
    def getMainMenu(self) -> IMainMenu:
        return WindowsMainMenu()
    def getMainWindow(self) -> IMainWindow:
        return WindowsMainWindow()

class LinuxGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> IStatusBar:
        return LinuxStatusBar()
    def getMainMenu(self) -> IMainMenu:
        return LinuxMainMenu()
    def getMainWindow(self) -> IMainWindow:
        return LinuxMainWindow()
"""
Клиентский класс, использующий фабрику для создания GUI
"""
class Application:
    def __init__(self, gui_factory: GuiAbstractFactory):
        self.__gui_factory = gui_factory

    def create_gui(self):
        main_window = self.__gui_factory.getMainWindow()
        status_bar = self.__gui_factory.getStatusBar()
        main_menu = self.__gui_factory.getMainMenu()
        main_menu.create()
        main_window.create()
        status_bar.create()

def create_factory(system_name: str) -> GuiAbstractFactory:
    factory_dict = {
        "Windows": WindowsGuiFactory,
        "Linux": LinuxGuiFactory
    }
    return factory_dict[system_name]()

if __name__ == '__main__':
    system_name = "Linux"
    ui = create_factory(system_name)
    app = Application(ui)
    app.create_gui()
"""
Created MAIN MENU for Linux
Created main WINDOW for Linux
Created status bar for Linux
"""

"""[-] МУТОРНО, НЕПОНЯТНО (сам код в main'e), СЛИШКОМ ДЛИННЫЙ ПРИМЕР =( [+] ЕЩЕ ОДИН ПРИМЕР КОДА """