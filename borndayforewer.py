def check_year_poet():
    global year_poet
    while not year_poet.isdigit():
        print('Введите целочисленное значение')
        year_poet = input('Год рождения Пушкина? :')


def check_day_poet():
    global birthday_poet
    while not birthday_poet.isdigit():
        print('Введите целочисленное значение')
        birthday_poet = input('День рождения Пушкина? :')


year_poet = input('Год рождения Пушкина? :')
check_year_poet()
while not int(year_poet) == 1799:
    year_poet = input('Год рождения Пушкина? :')
    check_year_poet()
if int(year_poet) == 1799:
    birthday_poet = input('День рождения Пушкина? :')
    check_day_poet()
    while not int(birthday_poet) == 6:
        birthday_poet = input('День рождения Пушкина? :')
        check_day_poet()
    print('Верно')
