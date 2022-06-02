class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, add):
        res_matrix = []

        if len(self.matrix) == len(add.matrix):
            res_matrix = [map(sum, zip(*i)) for i in zip(self.matrix, add.matrix)]
            return '\n'.join('\t'.join(map(str, row)) for row in res_matrix)
        else:
            raise ValueError('Размеры матриц не совпадают')


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


m1 = Matrix([[1, 1, 1],
             [2, 2, 2],
             [3, 3, 3]])

m2 = Matrix([[1, 1, 1],
             [2, 2, 2],
             [3, 3, 3]])

print(m1.__add__(m2))