k = input()
d = dict()
d = {char: 1 for char in ('а', 'в', 'е', 'и', 'н', 'о', 'р', 'с','т')}
d.update({char: 2 for char in ('д', 'к', 'л', 'м', 'п', 'у')})
d.update({char: 2 for char in ('d', 'g')})
d.update({char: 3 for char in ('b', 'c', 'm', 'p')})
d.update({char: 3 for char in ('б', 'г', 'ё', 'ь', 'я')})
d.update({char: 4 for char in ('f', 'h', 'v', 'w', 'y')})
d.update({char: 4 for char in ('й', 'ы')})
d.update({char: 5 for char in ('k',)})
d.update({char: 5 for char in ('ж', 'з', 'х', 'ц', 'ч')})
d.update({char: 8 for char in ('j', 'x')})
d.update({char: 8 for char in ('ш', 'э', 'ю')})
d.update({char: 10 for char in ('q', 'z')})
d.update({char: 10 for char in ('ф', 'щ', 'ъ')})
count = 0
for i in range(len(k)):
    count += d[k[i]] 
print(count)      
