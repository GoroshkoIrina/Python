class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weigth = None
        self.tickness = None

    def mass_count(self):
        self.weigth = 25
        self.tickness = 5
        return self._length * self._width * self.weigth * self.tickness / 1000


a = Road(5000, 20)
print('Потребуется', a.mass_count(), 'т. асфальта')