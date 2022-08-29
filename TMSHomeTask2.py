# Ex 1

multiples_of_7 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
first_five = multiples_of_7[:5]
assert [7, 14, 21, 28, 35] == first_five

# Ex 2

from collections import Counter

NUMBERS = [4, 1, 8, 4, 0, 2, 8, 1, 0, 4, 8]

count = Counter(NUMBERS)  # Получает словарь с ключем - значением элемента, значением - количество идентичных элементов в списке
item_list = list(count.items())
for i in range(len(count)):
    current_value = count.popitem()
    if current_value[1] > 1:
        for b in range(current_value[1] - 1):  # Если в списке несколько идентичных элементов, то цикл удаляет первые по списку дубликаты оставляя один
            NUMBERS.remove(current_value[0])
assert [2, 1, 0, 4, 8] == NUMBERS

new_dict = dict.fromkeys(NUMBERS)
abbreviated_list = list(new_dict.keys())
assert [2, 1, 0, 4, 8] == abbreviated_list
# Ex 3

set_list = set(NUMBERS)
new_list = list(set_list)
assert [0, 1, 2, 4, 8] == new_list

# Ex 4

CITIES = ('Minsk', 'Gomel', 'Mogivel', 'Orsha', 'Vitebsk', 'Grodno')
cities_list = list(CITIES)
cities_list.append('Brest')
assert ['Minsk', 'Gomel', 'Mogivel', 'Orsha', 'Vitebsk', 'Grodno', 'Brest'] == cities_list