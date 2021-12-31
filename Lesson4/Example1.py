def sal():
    try:
        time = float(input('Выработка в часах>> '))
        salary = int(input('Ставка в час(руб.)>> '))
        bonus = int(input('Премия (руб.)>> '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника>>  {res}')
    except ValueError:
        return print('Not a number')
sal()
