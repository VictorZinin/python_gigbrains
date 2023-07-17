"""
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
Они обратились к синоптикам, те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе.
"""

from random import randint

days = int(input('Введите количество дней: '))
max_len, count, temp = 0, 0, 0

for _ in range(days):
    temp += randint(-3, 3)
    print(temp, end=' ')
    if temp > 0:
        count += 1
        if count > max_len:
            max_len = count
    else:
        count = 0

print(f'\nМаксимальное количество теплых дней подряд - {max_len} дней')