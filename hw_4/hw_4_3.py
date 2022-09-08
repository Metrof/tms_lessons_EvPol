# Ex. 3
# На вход функции подается натуральное число n.
# Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n,
# а затем выводит его элементы построчно, то есть каждый на отдельной строке.

def make_square_list(list_range: int):
    square_list = [x ** 2 for x in range(1, list_range + 1)]
    print(*square_list, sep="\n")


try:
    input_range = abs(int(input('Введите размер списка: ')))
except ValueError:
    print("Введите натуральное число")
else:
    make_square_list(input_range)

