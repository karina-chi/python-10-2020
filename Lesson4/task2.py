# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random
"""Создаю список случайных чисел"""
random_list = []

while len(random_list) < 10:
    a = random.randint(0, 100)
    random_list.append(a)

print(random_list)

new_list = [number for i, number in enumerate(random_list) if i > 0 and random_list[i] > random_list[i - 1]]
print(new_list)
