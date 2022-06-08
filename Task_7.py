class Complex_Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма комплексных чисел равна: ')
        return Complex_Number(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        print(f'Произведение комплексных чисел равно: ')
        return Complex_Number((self.a * other.a) - (self.b * other.b), (self.a * other.b) + (self.b * other.a))

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


number1 = Complex_Number(7, 1)
number2 = Complex_Number(1, 8)
print(number1)
print(number2)
print(number1 + number2)
print(number1 * number2)