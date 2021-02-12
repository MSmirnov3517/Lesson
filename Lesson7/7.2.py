class Clothes:

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def full_area(self):
        return (self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)


class P(Clothes):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def area_p(self):
        return self.v / 6.5 + 0.5


class K(Clothes):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def area_k(self):
        return self.h * 2 + 0.3



# c_1 = Clothes(5, 10)
p = P(10, 2)
k = K(5, 1)
# print(p.full_area())
print(p.area_p())
print(p.full_area)
print(k.area_k())
