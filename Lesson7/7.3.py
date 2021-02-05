class Cell:

    def __init__(self, count):
        self.count = count
        print(count)

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count < other.count:
            print(f'так нельзя')
            return Cell(0)
        else:
            return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, length):
        rows = self.count // length
        tail = self.count % length
        return '\n'.join(['*' * length] * rows + (['*' * tail] if tail else []))


c = Cell(20)
c_2 = Cell(3)
print((c + c_2).make_order(10))
print((c - c_2).make_order(10))
print((c * c_2).make_order(10))
print((c / c_2).make_order(10))