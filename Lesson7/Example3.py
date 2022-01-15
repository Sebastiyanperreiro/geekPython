class Cell:
    def __init__(self, quant):
        self.quant = quant

    # Сложение реализовал по принципу слияния клеток. Все ячейки из обеих клеток переходят в третью, соответственно
    # первая и вторая клетки остаются с обнуленным количеством ячеек
    def __add__(self, other):
        res_quant = self.quant + other.quant
        self.quant = 0
        other.quant = 0
        return Cell(res_quant)

    # Вычитание реализовал по принципу нападения первой клетки на вторую. Первая клетка побеждает, если у нее больше
    # ячеек, тогда из первой клетки вычитается то количество клеток, которое было в второй клетке. Вторая клетка,
    # соответственно, обнуляется
    def __sub__(self, other):
        sub_res = self.quant - other.quant
        if sub_res >= 0:
            self.quant -= other.quant
            other.quant = 0
            return self
        else:
            print(f'Клетке {self} не хватает ячеек для вычитания')

    # Создается новая клетка с количеством ячеек, равным произведению количества ячеек обеих клеток. Клетки-родители
    # продолжают жить с тем же количеством ячеек
    def __mul__(self, other):
        res_quant = self.quant * other.quant
        return Cell(res_quant)

    # Создается новая клетка с количеством ячеек, равным делению количества ячеек в первой клетке на
    # количество во второй. Клетки-родители продолжают жить с тем же количеством ячеек
    def __truediv__(self, other):
        res_quant = self.quant // other.quant
        if res_quant:
            return Cell(res_quant)
        else:
            print(f'Клетке {self} не хватает ячеек для деления')

    def __str__(self):
        return f'{self.quant}'

    def make_order(self, num_in_range):
        cell_order = ''
        for el in range(1, self.quant+1):
            if not el % num_in_range:
                cell_order += '*\n'
            else:
                cell_order += '*'
        return cell_order


my_cell_1 = Cell(10)
my_cell_2 = Cell(15)

print(f'my_cell_1.quant: {my_cell_1.quant}, my_cell_2.quant: {my_cell_2.quant}')
# Сложение
cell_add = my_cell_1 + my_cell_2
print(f'Сложение:\nmy_cell_1.quant: {my_cell_1.quant}, my_cell_2.quant: {my_cell_2.quant}, cell_add.quant: {cell_add.quant}')

# Вычитание
my_cell_1 = Cell(10)
my_cell_2 = Cell(15)
cell_sub_1 = my_cell_1 - my_cell_2
my_cell_1 = Cell(15)
my_cell_2 = Cell(10)
cell_sub_2 = my_cell_1 - my_cell_2
print(f'Вычитание:\nmy_cell_1.quant: {my_cell_1.quant}, my_cell_2.quant: {my_cell_2.quant}, '
      f'cell_sub_2.quant: {cell_sub_2.quant}')

# Умножение
my_cell_1 = Cell(10)
my_cell_2 = Cell(15)
cell_mul = my_cell_1 * my_cell_2
print(f'Умножение:\nmy_cell_1.quant: {my_cell_1.quant}, my_cell_2.quant: {my_cell_2.quant}, '
      f'cell_mul.quant: {cell_mul.quant}')

# Деление
my_cell_1 = Cell(10)
my_cell_2 = Cell(15)
cell_div_1 = my_cell_1 / my_cell_2
my_cell_1 = Cell(35)
my_cell_2 = Cell(15)
cell_div_2 = my_cell_1 / my_cell_2
print(f'Деление:\nmy_cell_1.quant: {my_cell_1.quant}, my_cell_2.quant: {my_cell_2.quant}, '
      f'cell_div_2.quant: {cell_div_2.quant}')
#
my_cell_3 = Cell(11)
print(my_cell_3.make_order(4))