class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки')


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print('Пишет ручка')


class Pencil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print('Пишет карандаш')


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print('Пишет маркер')


a = Pen('1')
b = Pencil('2')
c = Handle('3')
a.draw()
b.draw()
c.draw()