# Ex. 1
# Есть список, содержащий кортежи [(1, 2), (3, 4), (5, 6)]
# Используя list comprehension получить список, содержащий сумму элементов кортежа

list_tutle = [(1, 2), (3, 4), (5, 6)]
sum_tutle = [sum(x) for x in list_tutle]
assert [3, 7, 11] == sum_tutle
