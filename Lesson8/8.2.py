"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""

class Except:

    def __init__(self, numb):
        self.numb = numb

    def integ(self):
        int_numb = []
        for el in self.numb.split('/'):
            el = int(el)
            int_numb.append(el)
        try:
            res = int_numb[0] / int_numb[1]
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        else:
            print(f"Все хорошо. Результат - {res}")


e = Except(input('введите пример в формате а/б '))
e.integ()
