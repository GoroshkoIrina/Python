class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print('Машина поехала')

    def stop(self):
        return print('Машина остановилась')

    def turn(self, direction):
        return print('Машина повернула', direction)

    def show_speed(self):
        return print('Текущая скорость:', self.speed)


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            return print('Превышение скорости:', self.speed)
        else:
            return print('Текущая скорость:', self.speed)


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            return print('Превышение скорости:', self.speed)
        else:
            return print('Текущая скорость:', self.speed)

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


first = TownCar(70, 'красный', 'Mercedes')
print(first.name, 'цвет:', first.color)
first.go()
first.show_speed()
first.turn('налево')
first.stop()
second = SportCar(150, 'синий', 'Renault')
print(second.name, 'цвет:', second.color)
second.go()
second.show_speed()
second.turn('направо')
second.stop()
third = WorkCar(50, 'черный', 'Audi')
print(third.name, 'цвет:', third.color)
third.go()
third.show_speed()
third.turn('назад')
third.stop()
fourth = PoliceCar(100, 'белый', 'Lada')
print(fourth.name, 'цвет:', fourth.color)
fourth.go()
fourth.show_speed()
fourth.turn('направо')
fourth.stop()