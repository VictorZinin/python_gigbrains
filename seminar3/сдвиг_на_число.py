"""
Дана последовательность чисел. Нужно сдвинуть на введеный пользователем сдвиг.
"""

from random import randint

print(lst := [randint(-5,5) for _ in range(10)]) #Оператор := называется оператором моржа и он присваивает значение выражения справа от него переменной слева, а затем возвращает значение этой переменной. 
shift = int(input('Введите сдвиг: '))
#print(lst[-shift:] + lst[:-shift]) # вырезаем и вставляем вперед
"""
for i in range(shift):
    lst.insert(0,lst.pop())# вырезает с конца и вставляет в начало 
print(lst)
"""
new_lst = []
for i in range (len(lst)):
    new_lst.append(lst[(i-shift) % len(lst)]) # добавляет в начало разницу 
print(new_lst)
