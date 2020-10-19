# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# Запускать данный скрипт с параметрами. Правая кнопка >>> edit {file_name} >>> parameters. Заполнять через пробел!

from sys import argv

script, production, rate, premium = argv
a = float(production)
b = float(rate)
c = float(premium)


def salary_calculation(hours, rate_in_hour, additional_money):
    return hours * rate_in_hour + additional_money


print(f'Заработная плата сотрудника составляет {salary_calculation(a, b, c)}')
