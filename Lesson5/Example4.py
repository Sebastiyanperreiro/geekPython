rus_numerals = {'0': 'Ноль', '1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять', '6': 'Шесть', '7': 'Семь', '8': 'Восемь', '9': 'Девять'}

with open('test_4.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read()
    english_numerals = (a_numeral for a_numeral in content.splitlines())

with open('test_4_new.txt', 'w', encoding='utf-8') as file_obj:
    while True:
        try:
            num = next(english_numerals).split(" — ")[1]
            file_obj.write(f'{rus_numerals[num]} — {num}\n')
        except StopIteration:
            break