# Ex. 5
# Написать ф-ю, которая выводит сегодняшнюю дату, текущее время и приветствие.
import datetime


def get_the_date():
    print(f'Добрый день! Сегодня {datetime.date.today()}, время - {datetime.datetime.now().time()}')


get_the_date()
