"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

number = int(input("Введи число: "))
power_two = 1
while power_two <= number:
    print(power_two)
    power_two *= 2  
