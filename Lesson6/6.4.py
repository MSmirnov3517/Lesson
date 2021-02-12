class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(self.speed)

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def turn_right(self):
        print(f'{self.name} повернула направо')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 60:
            print('превышение скорости')
        else:
            print(f'Текущая скорость {self.speed}')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)

class Police(Car):

    def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 40:
            print('превышение скорости')
        else:
            print(f'Текущая скорость {self.speed}')

lada = TownCar(30, 'red', 'Lada', False)
ford = SportCar(240, 'white', 'ford', False)
uaz = Police(100, 'blue', 'UAZ', True)
logan = WorkCar(100, 'red', 'logan', False)

lada.turn_left()
lada.show_speed()
print(ford.name, ford.speed, ford.color, ford.is_police)
logan.show_speed()
ford.show_speed()