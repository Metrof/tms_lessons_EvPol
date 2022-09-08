# Ex. 2
# Дан словарь. Создать новый словарь, поменяв местами ключ и значение

start_dict = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune'}
finish_dict = {start_dict[x]: x for x in start_dict}
assert {'Mercury': 1, 'Venus': 2, 'Earth': 3, 'Mars': 4, 'Jupiter': 5, 'Saturn': 6, 'Uranus': 7, 'Neptune': 8} == finish_dict
