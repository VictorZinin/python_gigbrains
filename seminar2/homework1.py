"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
from random import randint
count_coins = int(input('Введите количесвто монет: '))
count, coin = 0, 0
for _ in range (count_coins):
    coin = randint(0, 1)
    print(coin, end=' ')
    if coin == 0:
        count += 1
if count > count_coins - count:
    if count_coins == 1:
        print(f"\n {count_coins} монету надо перевернуть")
    elif count_coins == 2 or count_coins == 3 or count_coins == 4:
        print(f"\n {count_coins} монеты надо перевернуть")
    else :
        print(f"\n {count_coins} монет надо перевернуть")
else:
    if count == 1:
        print(f"\n {count} монету надо перевернуть")
    elif count == 2 or count == 3 or count == 4:
        print(f"\n {count} монеты надо перевернуть")
    else :
        print(f"\n {count} монет надо перевернуть")
