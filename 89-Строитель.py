"""Строитель
Нужно создать один большой обьект (с 10 аргументами)
Строитель - вместо этого применяем пошаговое постоение
Строитель предоставляет API для пошагового построения сложного обьекта"""

"""Нужно создать обзац из текста"""
"""
text = 'hello'
parts = ['<p>', text, '<p>']
print(''.join(parts)) # <p>hello<p>
"""
"""(Сложнее) У нас есть слова, мы хотим составить из них список html"""
"""
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f' <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))
"""
"""(Сработало, но уже сложно (нужно не забыть закрыть /ul, закрыть /li)
<ul>
 <li>hello</li>
 <li>world</li>
</ul>
"""
"""Решение - Строитель"""
class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}<{self.text}>')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name): # (Улучшение 2) API для юзера
        return HtmlBuilder(name)

class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name) # экземпляр элемента (который мы создаём)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
    def add_child_fluent(self, child_name, child_text): # (Улучшение 1) размерает вызвать несколько методов один за другим
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)

# builder = HtmlBuilder('ul')
builder = HtmlElement.create('ul') # (Улучшение 2)
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world') # (Улучшение 1)
print('Ordinary Builder:')
print(builder)
"""
<ul>
  <li>
    <hello>
  </li>
  <li>
    <world>
  </li>
</ul>
"""

