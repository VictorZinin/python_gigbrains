"""
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

def ArifmeticFiller():
    first =int(input("Введите первый элемент: "))
    step = int(input("Введите шаг прогрессии: "))
    ammount=int(input("Введите количество элементов: "))
    progressive =[first]
    for i in range(ammount):
        if i!=0:
            progressive.append(progressive[i-1]+step)
        print(i)
    return progressive
print(ArifmeticFiller())