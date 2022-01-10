class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    me = Position('Sebastiyan', 'Perreiro', 'DevOps engineer', 4500, 2000)
    me2 = Position('Себастьян', 'Перрейро', 'Top DevOps engineer', 55000, 15000)
    print(me.get_full_name())
    print(me.position)
    print(f'Total income: {me.get_total_income()}')
    print(me._income)
    print(me2.get_full_name())
    print(f'Total income: {me2.get_total_income()}')
    print(me2.position)
    print(me2._income)