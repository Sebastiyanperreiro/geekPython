class MyZeroDiv(Exception):
    def __init__(self, divided, divider):
        self.divided = divided
        self.divider = divider

    def __str__(self):
        return "Can't divide on Zero"


def dividing(div1, div2):
    if div2 == 0:
        raise MyZeroDiv(user_divided, user_divider)
    else:
        return div1 / div2


try:
    user_divided = float(input("Укажите делимое >> "))
    user_divider = float(input("Укажите делитель >> "))
    try:
        c = dividing(user_divided, user_divider)
        print(f'Результат >>> {c:.01f}')
    except MyZeroDiv as exception:
        print("Не могу разделить на ноль")
except ValueError:
    print('Неверный формат')
