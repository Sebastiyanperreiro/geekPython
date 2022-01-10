class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}.')



class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}.')


my_pen = Pen('Lacubo')
my_pencil = Pencil('Конструктор 2Т')
my_handle = Handle('ErichKrause')

my_pen.draw()
my_pencil.draw()
my_handle.draw()