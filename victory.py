# Born Kiany = 1964
# Born Chardi = 1977
# Born Lacosta = 1997
# Born Niletto = 1991
# Born Eljey = 1994

is_repeat = True
while is_repeat:
    success = 0
    failed = 0
    kiany_born = input('Год рождения Киану Ривза?')
    if int(kiany_born) == 1964:
        success += 1
    else:
        failed += 1
    tom_born = input('Год рождения Тома Харди?')
    if int(tom_born) == 1977:
        success += 1
    else:
        failed += 1
    lacosta_born = input('Год рождения Косты Лакосты?')
    if int(lacosta_born) == 1997:
        success += 1
    else:
        failed += 1
    niletto_born = input('Год рождения Niletto?')
    if int(niletto_born) == 1991:
        success += 1
    else:
        failed += 1
    eldjey_born = input('Год рождения Элджея?')
    if int(eldjey_born) == 1994:
        success += 1
    else:
        failed += 1
    print('Ваши правильные ответы: ', success)
    print('Процент правильных ответов: ', (success*100)/5, '%')
    print('Ваши неправильные ответы: ', failed)
    print('Процент неправильных ответов: ', (failed*100)/5, '%')
    is_repeat = input('Хотите повторить')
    if is_repeat == 'Да':
        is_repeat = True
    else:
        is_repeat = False
