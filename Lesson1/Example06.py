a = float(input("Введите результаты пробежки первого дня в км: "))
b = float(input("Введите желаемый результат в км: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(f"Вы достигнете требуемых показателей на %.d день" % day)