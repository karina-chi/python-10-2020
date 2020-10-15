# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов

def my_func(arg_1, arg_2, arg_3):
    new_list = [arg_1, arg_2, arg_3]
    new_list.remove(min(arg_1, arg_2, arg_3))
    return sum(new_list)


print(my_func(7, 5, 4))
