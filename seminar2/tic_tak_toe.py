"""
игра в крестики нолики
"""

print(f'Приветсвую игроки! Это игра "крестики - нолики".\nЯ нарисовал поле:')
print(f' | |  ', f'\n | | ', f'\n | | ')
answer = str(input('Если готовы сыграть пишите "да"\n'))
if answer == 'да':
    name_first = str(input('Отлично! Расскажу вам организационный момент.\nКак вы можете заметить, я нарисовал поле 3 x 3.\nОпределите, кто будет "X"? '))
    name_sec = str(input('Определите, кто будет "0"? '))
    first = str(input('Кто первый ходит? '))
    if first != name_first:
        name_first, name_sec = name_sec, name_first
else:
    print("Очень жаль, захотите поиграть - я тут. Пока!")
i = 'продолжим'
count = 1
x1_y1, x1_y2, x1_y3 = ' |', ' ', '| '
x2_y1, x2_y2, x2_y3 = ' |', ' ', '| '
x3_y1, x3_y2, x3_y3 = ' |', ' ', '| '
var_1 = False
var_2 = False
var_3 = False
var_4 = False
var_5 = False
var_6 = False
var_7 = False
var_8 = False
while (var_1 != True) and (var_2 != True) and (var_3 != True) and (var_4 != True) and (var_5 != True) and (var_6 != True) and (var_7 != True) and (var_8 != True) and count != 10:
    if count % 2 == 1:
        x, y = map(int, input(f"{name_first}, введи координаты: ").split())
        if x == 1:
            if y == 1:
                x1_y1 = 'X|'
            elif y == 2:
                x1_y2 = 'X'
            elif y == 3:
                x1_y3 = '|X'
            else:
                print("Упс, ошибка. Попробуй еще раз!")
        elif x == 2:
            if y == 1:
                x2_y1 = 'X|'
            elif y == 2:
                x2_y2 = 'X'
            elif y == 3:
                x2_y3 = '|X'
            else:
                print("Упс, ошибка. Попробуй еще раз!")    
        elif x == 3:
            if y == 1:
                x3_y1 = 'X|'
            elif y == 2:
                x3_y2 = 'X'
            elif y == 3:
                x3_y3 = '|X'
            else:
                print("Упс, ошибка. Попробуй еще раз!")
        else:
            print("Упс, ошибка. Попробуй еще раз!") 
    else:
            a, b = map(int, input(f"{name_sec}, введи координаты: ").split())
            if a == 1:
                if b == 1:
                    x1_y1 = '0|'
                elif b == 2:
                    x1_y2= '0'
                elif b == 3:
                    x1_y3 = '|0'
                else:
                    print("Упс, ошибка. Попробуй еще раз!")
            elif a == 2:
                if b == 1:
                    x2_y1 = '0|'
                elif b == 2:
                    x2_y2= '0'
                elif b == 3:
                    x2_y3 = '|0'
                else:
                    print("Упс, ошибка. Попробуй еще раз!") 
            elif a == 3:
                if b == 1:
                    x3_y1 = '0|'
                elif b == 2:
                    x3_y2= '0'
                elif b == 3:
                    x3_y3 = '|0'
                else:
                    print("Упс, ошибка. Попробуй еще раз!")
            else:
                    print("Упс, ошибка. Попробуй еще раз!")
    print(f"{x1_y1}{x1_y2}{x1_y3}\n{x2_y1}{x2_y2}{x2_y3}\n{x3_y1}{x3_y2}{x3_y3}")
    x1_y1_1, x1_y2_1, x1_y3_1 = x1_y1.replace('|', ''), x1_y2.replace('|', ''), x1_y3.replace('|', '')
    x2_y1_2, x2_y2_2, x2_y3_2 = x2_y1.replace('|', ''), x2_y2.replace('|', ''), x2_y3.replace('|', '')
    x3_y1_3, x3_y2_3, x3_y3_3 = x3_y1.replace('|', ''), x3_y2.replace('|', ''), x3_y3.replace('|', '')
    var_1 = (x1_y1_1 == x1_y2_1 == x1_y3_1 == 'X') or (x1_y1_1 == x1_y2_1 == x1_y3_1 == '0') 
    var_2 = (x2_y1_2 == x2_y2_2 == x2_y3_2 == 'X') or (x2_y1_2 == x2_y2_2 == x2_y3_2 == '0')
    var_3 = (x3_y1_3 == x3_y2_3 == x3_y3_3 == 'X') or (x3_y1_3 == x3_y2_3 == x3_y3_3 == '0')
    var_4 = (x1_y1_1 == x2_y1_2 == x3_y1_3 == 'X') or ('0' == x1_y1_1 == x2_y1_2 == x3_y1_3)
    var_5 = (x1_y2_1 == x2_y2_2 == x3_y2_3 == 'X') or ('0' == x1_y2_1 == x2_y2_2 == x3_y2_3)
    var_6 = (x1_y3_1 == x2_y3_2 == x3_y3_3 == 'X') or ('0' == x1_y3_1 == x2_y3_2 == x3_y3_3)
    var_7 = (x1_y1_1 == x2_y2_2 == x3_y3_3 == 'X') or ('0' == x1_y1_1 == x2_y2_2 == x3_y3_3)
    var_8 = (x3_y1_3 == x2_y2_2 == x1_y3_1 == 'X') or ('0' == x3_y1_3 == x2_y2_2 == x1_y3_1)
    count += 1
if count % 2 != 0 and count != 10:
    print(f'Поздравляю, {name_sec}! Ты выиграл!!!')
elif count % 2 == 0 and count != 10:
    print(f'Поздравляю, {name_first}! Ты выиграл!!!')
else:
    print(f'У вас ничья.')