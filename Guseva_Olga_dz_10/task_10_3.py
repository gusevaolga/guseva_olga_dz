class Cell:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Cell(self.value + other.value)

    def __str__(self):
        return str(self.value)

    def __sub__(self, other):
        result = self.value - other.value
        if result > 0:
            return Cell(self.value - other.value)
        else:
            raise Exception("Can't sub two cells")

    def __mul__(self, other):
        return Cell(self.value * other.value)

    def __floordiv__(self, other):
        return Cell(self.value // other.value)

    def __truediv__(self, other):
        return Cell(self.value / other.value)

    def make_order(self, count):
        full_rows = self.value // count
        row = f'{"*" * count} \n' * full_rows + f'{"*" * (self.value % count)}'
        return row


cell_1 = Cell(44)
print(cell_1.make_order(7))
print(cell_1)
