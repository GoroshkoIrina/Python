class Cell:
    def __init__(self, quantity):
        if quantity < 0:
            raise ValueError('Количество ячеек не может быть отрицательным')
        else:
            self.quantity = int(quantity)

    def __str__(self):
        return f'Количество ячеек клетки: {self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity < other.quantity:
            return 'Операция вычитания невозможна'
        else:
            return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __floordiv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, row_size):
        result = ''
        for i in range(int(self.quantity / row_size)):
            result += f'{"*" * row_size}\\n'
        result += f'{"*" * (self.quantity % row_size)}'
        return result

cell1 = Cell(15)
cell2 = Cell(40)
print(cell1)
print(cell2)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell2 * cell1)
print(cell2 / cell1)
print(cell1 // cell2)
print(cell1.make_order(3))
print(cell2.make_order(7))
