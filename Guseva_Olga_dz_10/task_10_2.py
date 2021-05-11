from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def calc_expenditure(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def calc_expenditure(self):
        count = self.size / 6.5 + 0.5
        return count

class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def calc_expenditure(self):
        count = self.height + 0.3
        return count


coat = Coat(25)
print(coat.calc_expenditure)

suit = Suit(133)
print(suit.calc_expenditure)
