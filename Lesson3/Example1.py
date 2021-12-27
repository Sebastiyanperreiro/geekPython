def div(*args):
    try:
        arg1 = int(input("Введите число>> "))
        arg2 = int(input("Введите делитель>> "))
        res = arg1 / arg2
    except ValueError:
        return 'Ощибка!!!'
    except ZeroDivisionError:
        return "Неверный делитель! Вы не можете использовать 0 как делитель"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Неправильно! Делитель не может быть 0")
    '''


print(f'Результат = {div()}')
