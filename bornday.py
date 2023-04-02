year_poet = input('Год рождения Пушкина? :')
while not year_poet.isdigit():
    print('Введите целочисленное значение')
    year_poet = input('Год рождения Пушкина? :')
if int(year_poet) == 1799:
    birthday_poet = input('День рождения Пушкина? :')
    if int(birthday_poet) == 6:
        print('Верно')
    else:
        print('Неверно')
else:
    print('Неверный год')