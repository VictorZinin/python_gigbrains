"""
Даны два неупорядоченных набора цеых чисел. Выдать в порядке возрастания все те числа, которые встречаются в обоих наборах.
"""

n = int(input('Введите кол-во чисел множества n: '))
m = int(input('Введите кол-во чисел множества m: '))
count_n = 0
count_m = 0
max_list = []
min_list = []
while count_n < n:
    max_list.append(input('Введите число в набор n: '))
    count_n += 1
while count_m < m:
    min_list.append(input('Введите число в набор m: '))
    count_m += 1
print(max_list)
print(min_list)
if len(max_list) < len(min_list):
    max_list, min_list = min_list, max_list
tot_dict = dict.fromkeys(min_list)
total = []
for i in max_list:
    if i in tot_dict:
        total.append(i)
for i in range(len(total)-1):
    for j in range(0, len(total)-i-1):
        if total[j] > total[j+1]:
            total[j], total[j+1] = total[j+1], total[j]
print(total)


