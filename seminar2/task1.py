"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, адругой для тещи.
 Понятно, что для себя нужно выбрать арбуз потяжелей, для тещи полегче.
   Новот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N –количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число –это масса соответствующего арбуза. Всечисла натуральные и не превышают 30000.
"""

from random import randint

count_wm = int(input('Введите количество арбузов: '))

max_wm = float('-inf')
min_wm = float('inf')
print(f'Перед вами {count_wm} арбузов:')
for _ in range(count_wm):
    current_wm = randint(1000, 30000)
    print(current_wm, end=' ')
    if max_wm < current_wm:
        max_wm = current_wm
    if min_wm > current_wm:
        min_wm = current_wm
print(f'\nСамый тяжелый арбуз - {max_wm} гр\nСамый легкий арбуз - {min_wm} гр')