# Python-Patterns
GoF Patterns (usefull list of examples)

https://refactoring.guru/ru/design-patterns/catalog 

## 🏗 Порождающие - 
<p>Отвечают за удобное и безопасное создание новых объектов или даже целых семейств объектов.</p>

<details><summary>Абстрактная фабрика <b>Пример. Японская фабрика авто / Русская фабрика авто</b>  <b></b></summary>
Порождающий паттерн<br>

```Абстрактная фабрика (Abstract Factory)``` - предоставляет интерфейс взаиосвязанных/взаимоЗависимых обьектов<br>
- когда прога должна быть независима от процессов и типов новых создаваемых обьектов<br>
- когда нужно создавать группы взаимосвязанных обьектов<br>
[+] изолирует конкретные классы<br>
[+] упрощает замену семейств продуктов<br>
[+] гарантирует сочитаемость продуктов<br>
[-] сложность добавления/поддержки нового вида продуктов<br>

```Пример. Японская фабрика авто / Русская фабрика авто```

</details>


<details><summary>Строитель (Builder)  <b>Cоздание Телефона (Android и IPhone)</b></summary>
```Порождающий паттерн

```Строитель (Builder)``` - предоставляет способ создания составного обьекта<br>
[+] позволяет изменять внутреннее пердставление продукта<br>
```Пример. Cоздание Телефона (Android и IPhone)```
</details>


<details><summary>Прототип  <b>использование copy.deepcopy()</b></summary>
</details>


<details><summary>SINDGLETON   <b>только один экземпляр DataBase</b></summary>

Порождающий паттерн<br>
(Отвечают за удобное и безопасное создание новых объектов( или даже целых семейств объектов))<br>

```SINDGLETON```<br>
смысл - ```в проге всегда может существовать только один экземпляр DataBase``` (или Логгирования, Кеш, Аутентификация)
</details>


<details><summary>АДАПТЕР  <b>JSON > XML</b></summary>

```АДАПТЕР```<br>
совмещать классы которые не могут быть совместимыми<br>
```
JSON 100 cls, 100 intf
XML
```

</details>

[//]: # (# #########################Структурные######################################)

## 🏗 Структурные
<p>Отвечают за построение удобных в поддержке иерархий классов.</p>

<details><summary>Мост (Bridge)  <b>DB/File >> Email/TgBot</b></summary>

Структурный

```Мост``` - разделяет абстракцию и реализацию так, чтобы они могли изменяться независимо<br>
(для реализации Моста -  применили абстракции IDataReader и Sender)<br>

```
Данные из БД: отправлены при помощи Email
Данные из Файла: отправлены при помощи Email
Данные из БД: отправлены при помощи Telegram бота
```
</details>

<details><summary>Компоновщик <b>Выпадающее меню</b></summary>

Структурный

```Компоновщик``` - обьединяет объекты в древовидную структуру для представления иерархии<br>
(Компоновщик - позволяет клиентам обращаться к отдельным обьектам и к группам обьектов одинаково)<br>
```Пример. Выпадающее меню```<br>
```
файл->Создать->Проект...
файл->Создать->Репозиторий...
файл->Открыть->Решение...
файл->Открыть->Папка...

файл->Открыть->Решение...
файл->Открыть->Папка...
```
</details>

<details><summary>Фасад (Facade) <b>Работа МаркетПлейса</b></summary>

Структурный

```Фасад (Facade)``` - позволяет скрыть сложность системы путём сведения всех (возможных внешних) вызовов<br>
 к одному обьекту (делегирующему их соответствующим обьектам системы)<br>

Фасад - применяеться для установки некоего рода политики по отношению к другой группе обьектов<br>
```Пример - Работа МаркетПлейса и его составных подразделений```<br>
```
Получение продукции от производителя
Размещение на сайте
Добавление товара в БД

Оплата поставщику (за товар) с удержанием комисси за продажу продукции
Удаление с сайта
Удаление товара из БД
```
</details>

<details><summary>Легковес (Flyweight)  <b>Учёт ИТшников разных компаний (приехавших на IT конфренцию)</b></summary>

Структурный

```Легковес (Flyweight)``` - позволяет вместить большее количество обьектов (в отведённую оперативную память)<br>
[+] Легковес экономит память, выделяя и сохраняя общие параметры объектов.<br>
[-] расходуеться процессорное время (на поиск)<br>
[-] изза введения доп классов (усложняеться код проги)<br>
```Пример. Учёт ИТшников разных компаний (приехавших на IT конфренцию)```<br>
```
Фабрика легковесов: Всего 4 записей.
Microsoft_Управляющий
Google_Android-разработчик
Google_Web-разработчик
Apple_IPhone-разработчик

Фабрика легковесов: Извлекаем данные из имеющихся записей по ключу Google_Web-разработчик.
Отображаем новые данные: общие - Google_Web-разработчик и уникальные Борис_AM-17234332

Фабрика легковесов: Общий обьект по ключу Apple_Управляющий не найден. Создаем новый.
Отображаем новые данные: общие - Apple_Управляющий и уникальные Александр_DE-2211032

Фабрика легковесов: Всего 5 записей.
Microsoft_Управляющий
Google_Android-разработчик
Google_Web-разработчик
Apple_IPhone-разработчик
Apple_Управляющий
```

</details>

<details><summary>Заместитель (Proxy)  <b>Работа (кэша) Веб Браузера</b></summary>

```Заместитель (Proxy)``` - вводим обьект (который контролирует доступ к другому обьекту) перехватывая все вызовы к нему<br>
([+] в web app - снижаеться кол-во запросов к серверу (в нём применяеться КЕШИРОВАНИЕ ранее полученных данных)<br>
```Пример. Работа (кэша) Веб Браузера```<br>
```
Это страница 1
Это страница 2
Это страница 3
из кеша: Это страница 2
```

</details>


[//]: # (# ####################### Поведенческие###################################)

## 🏗 Поведенческие
<p>Решают задачи эффективного и безопасного взаимодействия между объектами программы.</p>

<details><summary>Цепочка обязанностей (Chain of responsibility)  <b>Как разные этапы постройки дома - возлагаються на разных строителей</b></summary>

Поведенческий

```Цепочка обязанностей (Chain of responsibility)``` - он нужен для организации в системе уровней ответственности<br>
```Пример. Как разные этапы постройки дома - возлагаються на разных строителей```<br>
```
Проектировщик выполнил команду: спроектировать дом
Плотник выполнил команду: класть кирпич
Рабочий внутренней отделки выполнил команду: клеить обои
провести проводку - никто не умеет это делать =(
```

</details>


<details><summary>Команда (Command)  <b>Пульт управления Конвеером</b></summary>

Поведенческий

```Команда (Command)``` - обьект используеться для инкапсуляции всей информации нужной для выполнения/вызова обьекта (в будущем)<br>
```Пример. Пульт управления Конвеером```<br>
```
Конвейер запущен
Увеличена скорость конвеера
Снижена скорость конвеера
Конвейер остановлен
```

</details>


<details><summary>Посредник (Mediator)  <b>Заказчик > Project Manager(Mediator) >> Designer >> Employee</b></summary>

Поведенческий

```Посредник (Mediator)``` - позволяет уменьшить связанность множества классов между собой<br>
(благодаря перемещению этих связей в один класс-посредник)<br>
```Пример. Заказчик > Project Manager(Mediator) >> Designer >> Employee```<br>
```
->Директор дал команду: Проектировать
<-Дизайнер освобождён от работы

<-Дизайнер в работе
->Директор знает, что дизайнер уже работает
<-Дизайнер занят
```

</details>


<details><summary>Снимок (Memento) <b>Система анализа работы Биржи</b></summary>

Поведенческий

```Снимок (Memento)``` - позволяет сохранять и восстанавливать прошлое состояние обьектов<br>
(не раскрывая подробности их реализации)<br>
[+] не нарушает инкапсуляцию обьекта<br>
[+] упрощает его структуру<br>
[-] затраты памяти (выделяемой при частом создании снимка состояния)<br>
```Пример. Система анализа работы Биржи```<br>
```
Dollars:  10
Euro:  10
---- USD sell, EURO buy --------
Dollars:  9
Euro:  11
-------- SAVE ---------
---- USD sell, EURO buy --------
Dollars:  8
Euro:  12
-------- UNDO --------
Dollars:  9
Euro:  11
```

</details>


<details><summary>Наблюдатель (Observer) <b>Система наблюдения за ценой товара (Покупателем и Оптовым покупателем)</b></summary>

Поведенческий

`Наблюдатель (Observer)` - позволяет одним обьектам наблюдать (и реагировать на события) (происходящие в других обьектах)<br>
`Пример. Система наблюдения за ценой товара (Покупателем и Оптовым покупателем)`<br>
```
Покупатель закупил товар по цене 320
Оптовик закупил товар по цене 280
```

</details>

<details><summary>Состояние (State) <b>Светофор</b></summary>

Поведенческий

`Состояние (State)` - позволяет обьектам менять поведение (в зависимости от своего состояния)<br>
[+] где нужно избавиться от (большого числа) If конструкций<br>
`Пример. Светофор`<br>
```
Из желтого в красный цвет
Красный цвет
Из красного в желтый
Из желтого в зеленый
Зеленый цвет
```

</details>

<details><summary>Стратегия (Strategy) <b>Система парсинга новостей с различных инфо-ресурсов (применяя к каждому из них свою стратегию парсинга)</b></summary>

Поведенческий

`Стратегия (Strategy)` - он определяет семейство схожих алгоритмов (помещает каждый из них в собственный класс)<br>
[+] паттерн изолирует код алгоритмов от остальных классов<br>
[+] алгоритмы можно быстро заменять во время работы проги<br>
`Пример. Система парсинга новостей с различных инфо-ресурсов (применяя к каждому из них свою стратегию парсинга)`<br>
```
Парсинг новостного сайта: https://news.com
Парсинг ленты новостей социальной сети: https://www.facebook.com/groups/1278692272467147
Парсинг канала мессенджера Telegram: @news_channel_telegram
```

</details>

<details><summary>Шаблонный метод (Template method) <b>Передатчик речи (может быть аналоговым и цифровым)</b></summary>

Поведенческий

`Шаблонный метод (Template method)` - определяющий основу алгоритма<br>
(и позволяющий наследникам переобределять некоторые шаги алгоритма (не изменяя его структуру вцелом))<br>
[+] облегчает повторное использование кода<br>
`Пример. Передатчик речи (может быть аналоговым и цифровым)`<br>
```
Запись фрагмента речи
Модуляция аналогового сигнала
Передача сигнала по радиоканалу

Запись фрагмента речи
Дискретизация записанного фрагмента
Оцифровка
Модуляция ЦИФРОВОГО сигнала
Передача сигнала по радиоканалу
```

</details>

<details><summary>Посетитель (Visitor) <b>Отдыхающий посещает различные места в городе))</b></summary>

Поведенческий

`Посетитель (Visitor)` - позволяет добавлять в прогу новые операции (не изменяя классы обьектов (над которыми эти операции могут выполняться))<br>
[+] обьединяет родственные операции в одном классе<br>
[+] упрощает добавление операций (работающийх со сложными структурами обьектов)<br>
[-] возможно нарушение инкапсуляции элементов<br>
`Пример. Отдыхающий посещает различные места в городе))`<br>
```
Слон в зоопарке
Кино - Властелин колец
Клоун в цирке
```
</details>