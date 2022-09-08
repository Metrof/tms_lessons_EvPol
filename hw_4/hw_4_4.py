# Ex. 4
# Ф-я принимает список целых чисел и возвращает минимальное число, максимальное число, среднее-арифметическое.

def get_min_sum_max(numbers: list) -> list:
    return_list = [min(numbers), max(numbers), sum(numbers)]
    return return_list


assert get_min_sum_max([5, 3, 1, 10]) == [1, 10, 19]
