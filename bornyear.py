born_poet = input('Когда родился Пушкин А.А? :')
while not born_poet.isdigit():
    print('Введите целочисленное значение')
    born_poet = input('Когда родился Пушкин А.А? :')
if int(born_poet) == 1799:
    print('Верно')
else:
    print('Неверно')