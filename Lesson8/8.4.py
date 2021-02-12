"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных."""


class Store:

    def __init__(self):
        self._my_store = {}
        
    def add_store(self, unit):
        self._my_store.setdefault(unit.group_name(), []).append(unit)

    @property
    def my_store(self):
        return self._my_store


class Sklad:

    def __init__(self, model, year, name, count):
        self.model = model
        self.year = year
        self.name = name
        self.count = count
        self.group = self.__class__.__name__

        try:
            self.count = int(self.count)
        except ValueError:
            print('Количество вводите числом пожалуйста')
            exit()

    def group_name(self):
            return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.model} {self.year} {self.count}'

class Printer(Sklad):

    def __init__(self, model, year, name, count, power=1000):
        super().__init__(model, year, name, count)
        self.power = power

    def __repr__(self):
        return f'{self.name} {self.model} {self.year} {self.count} {self.power}'

    def print(self):
        print('Выполнена печать')


class Scanner(Sklad):

    def __init__(self, model, year, name, count):
        super().__init__(model, year, name, count)


    def scan(self):
        print('Выполнено сканирование')


class Xerox(Sklad):
    def __init__(self, model, year, name, count):
        super(Xerox, self).__init__(model, year, name, count)

    def copy(self):
        print('Выполнено конпирование')


store = Store()
printer = Printer('Sony', 1988, 'pw - 15', 5, 500)
store.add_store(printer)
printer2 = Printer('Sony', 1988, 'pw - 15', 10)
store.add_store(printer2)
xerox = Xerox('xerx',2020, 'ssa', 15)
store.add_store(xerox)
print(store.my_store)
