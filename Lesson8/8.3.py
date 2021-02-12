"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться"""


class Inc_text:

    def __init__(self):
        self.list = []

    def enter(self):
        while True:
            numb = input('Вводите числа, после каждого жмякайте Enter. Как надоест введите "q" - ')
            if numb == 'q' or numb == 'Q':
                break
            else:
                try:
                    numb = int(numb)
                except ValueError:
                    print(' Введите число, а не строку')
                else:
                    self.list.append(numb)
        return self.list


i = Inc_text()
print(i.enter())
