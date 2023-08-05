"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
"""

from random import randint

def FindIndexes(list, area, index=0):
    while(index < len(list)):
        if list[index] >= area[0] and list [index] <= area[1]:
            print(f"{index}", end=" ")
        index += 1

list = [randint(0,1000) for i in range (randint(10,100))]
print(list)
FindIndexes(list,[100, 500])