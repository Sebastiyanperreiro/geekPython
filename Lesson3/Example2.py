name = input('Введите имя>>')
surname = input('Введите фамилию>>')
year = int(input('Введите год рождения>>'))
city = input('Введите город проживания>>')
email = input('Введите электронную почту>>')
telephone = input('Введите номер телефона>>')


def my_func(surname, name, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(f"Фамилия={surname}, Имя={name}, Год рождения={year}, Город проживания={city}, Электронная почта={email}, Телефон={telephone}")

