class Stationery():

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Теперь мы рисуем {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Сейчас у нас в руках  {self.title}')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pencil.draw()
pen.draw()
handle.draw()
