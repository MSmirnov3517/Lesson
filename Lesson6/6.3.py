class Worker:

    name = 'Mikhail'
    surname = 'Smirnov'
    position = 'Student'
    _income = {'wage': 100000, 'bonus': 50000}

class Position(Worker):
    def get_full_name(self):
        print(Worker.name, Worker.surname)

    def get_total_income(self):
        print(Worker._income['wage'] + Worker._income['bonus'])

g = Position()

g.get_full_name()
g.get_total_income()
