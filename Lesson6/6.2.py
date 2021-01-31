class Road:
    _lenght = int(input('Введите длину дороги '))
    _width = int(input('Введите ширину дороги '))
    mas = 0

    def mass(self):
        mas = Road._lenght * Road._width * 25 * 5 / 1000
        print(f'{mas} т')

run = Road()
run.mass()
