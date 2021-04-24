class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки РУЧКОЙ')

class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки КАРАНДАШОМ')

class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки МАРКЕРОМ')


pen = Pen('pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
handle = Handle('handle')
handle.draw()