# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(arg_1, arg_2):
    return arg_1 / arg_2

var_1 = int(input("Введите делимое: "))
var_2 = int(input("Введите делитель: "))

try:
    print(f'{var_1} : {var_2} = {my_division(var_1, var_2)}')
except ZeroDivisionError:
    print("На ноль делить нельзя")
