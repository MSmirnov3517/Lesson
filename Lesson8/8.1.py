"""1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def integer(cls, date):
        int_date = []
        for el in date.split('-'):
            el = int(el)
            int_date.append(el)
        return int_date

    @staticmethod
    def valid(date):
        if date[0] >= 31:
            print('В месяце не может быть столько дней!')
        elif date[1] > 12:
            print('В году только 12 месяцев :) ')
        elif date[2] > 2036:
            print('Так далеко я бы не заглядывал :) ')
        else:
            print('oK')


print(Date.integer('10-13-2005'))
Date.valid([32, 10, 2005])
