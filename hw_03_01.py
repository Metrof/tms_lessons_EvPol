# Ex. 1 Ввести предложение, состоящее из двух слов.
# Поменять местами слова, добавить "!" в начало и конец, слова разделить 3 символами (" ", "!", " ")
# Пример
# "hello world" --> "world ! hello"
# Задание выполнить разными способами форматирования.

original_string = 'hello world'
first_word = original_string[:5]
second_word = original_string[6:11]
reformat_string = second_word + ' ' + '!' + ' ' + first_word
assert 'world ! hello' == reformat_string

divided_string = original_string.split(' ')
reformat_string_v2 = divided_string[1] + ' ' + '!' + ' ' + divided_string[0]
assert 'world ! hello' == reformat_string_v2

# Ex. 2
# Написать программу, которая получает имя и возраст пользователя, проверяет возраст и выдает приветственное сообщение
# в зависимости от возраста:
# - меньше нуля или ноль или не число: "Ошибка, повторите ввод"
# - больше 0 до 10 не включая: "Привет, малыш {имя}!"
# - от 10 до 18 включая: "Как дела {имя}?"
# - больше 18 и включая 120: "Что желаете {имя}?"
# - в противном случае: "{имя} вы лжете - столько не живут"
#
# Ex. 3
# Добавить в ex.2 бесконечный цикл.
# Выход из цикла сделать через ввод симолов "Q", "q"
looping = True


def hello_func():
    try:
        age = int(input('Введите возраст: '))
        assert age > 0
    except (ValueError, AssertionError):
        print("Ошибка, повторите ввод")
        return

    name = input('\nВведите имя: ')
    if age > 120:
        print(f"{name} вы лжете - столько не живут")
        return
    hello_mess_func(age, name)  # подбирает подходящее сообщение


def hello_mess_func(age: int, name: str):
    if 0 < age <= 10:
        print(f"\nПривет, малыш {name}!")
    elif 10 < age <= 18:
        print(f"\nКак дела {name}?")
    else:
        print(f"\nЧто желаете {name}?")


while looping:
    hello_func()
    user_char = str(input('\nЕсли желаете завершить цикл нажмите "Q"'))
    user_char = user_char.title()
    if user_char == 'Q': looping = False

# Ex.4
# Ввести целое число N. Получить сумму кубов всех целых чисел от 1 до N (включая).
# Реализовать через while и for.

user_int = int(input('Введите целое число: '))

result_sum_from_for = sum(i ** 2 for i in range(1, user_int + 1))  # реализация через for

counter = 0
result_sum_from_while = 0

while counter <= user_int:  # реализация с помощью while
    result_sum_from_while += counter ** 2
    counter += 1

assert result_sum_from_for == result_sum_from_while

# Ex 5. Реализовать вычисление факториала с помощью цикла while и for.
# Продумать область допустимых значений.
# Добавить проверки, исключаютщие бесконечный цикл.
# Написать тесты на различные варианты.
import math


def factorial_func(value):
    factorial = 1
    if value == 0:
        print('Недопустимое значение')
        return
    elif value < 0:
        value = abs(value)

    for i in range(1, value + 1):  # реализация с помощью for
        factorial *= i
    assert math.factorial(value) == factorial

    factorial = 1
    current_number = 1
    while current_number <= value:  # реализация с помощью while
        factorial *= current_number
        current_number += 1
    assert math.factorial(value) == factorial


try:
    user_factorial_int = int(input('\nВведите целое число: '))
except ValueError:
    print("Введите число")
else:
    factorial_func(user_factorial_int)


# Ex. 6 Написать программу в которой нужно будет угадывать число.
# Продумать диапазон чисел (будут жестко заданы или задаваться самим пользователем)
import random

number_list_file = open('numberArray.txt', 'r')
number_list = number_list_file.read()
number_list = number_list.split(' ')  # преобразуем строку с цифрами в список
number_list = [int(n) for n in number_list]
number_list_file.close()

start = 'Да'


def Game_process():
    main_num = number_list[random.randrange(0, len(number_list) - 1)]  # Выбирается случайное число
    current_attempt = 0
    while current_attempt < 3:
        try:
            player_num = int(input("\nВведите потенциальное число: "))
        except ValueError:
            print('Необходимо ввести число')
            continue
        if player_num == main_num:
            return 'Все верно, вы выйграли!'
        else:
            current_attempt = current_attempt + 1
            print('Ответ неверный. Количество попыток: ', 3 - current_attempt)
            if current_attempt == 3:
                return 'Вы проиграли!'


def Game():
    print('\nВы должны угадать число')
    print('У вас 3 попытки')
    print('Вот список возможных чисел: 10, 66, 777, 2007, 2077, 0')

    print(Game_process())

    global start
    start = str(input('\nЖелаете снова сыграть?("Нет", "Да") '))
    start = start.title()


while start == 'Да':
    Game()

print('\nВсего доброго!')