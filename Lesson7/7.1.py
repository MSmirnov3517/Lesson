class Matrix:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        new_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for x in range(3):
            for y in range(3):
                new_a[x][y] = self.a[x][y] + other.a[x][y]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in new_a]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.a]))


m_1 = Matrix([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
m_2 = Matrix([[2, 3, 4],
              [5, 6, 7],
              [7, 8, 9]])

print(m_1.__str__())
print(m_1 + m_2)
