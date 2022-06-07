from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def count_material(self):
        pass


class Coat(Clothes):

    @property
    def count_material(self):
        print(f'Расход ткани = {self.param/6.5 + 0.5} м')


class Suit(Clothes):

    @property
    def count_material(self):
        print(f'Расход ткани = {2*self.param + 0.3} м')


coat = Coat(10)
coat.count_material

suit = Suit(10)
suit.count_material

