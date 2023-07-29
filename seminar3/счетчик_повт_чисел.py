"""
программа принимает на вход строку и считает сколько раз число уже встречалось.
"""

number = input('Введите строку: ')
count_dict = {}
for i in number:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
    print (f'{i}' + (f'_{count_dict[i]-1}' if count_dict[i] > 1 else ' '), end=' ')