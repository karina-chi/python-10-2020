proceeds = int(input("Введите размер выручки фирмы за месяц: "))
costs = int(input("Введите количество издержек фирмы за месяц: "))
profit = "Фирма работает с прибылью."
loss = "Фирма работает с убытками."
if proceeds > costs:
    print(profit)
    profit_margin = (proceeds - costs) / proceeds * 100
    print("Рентабельность выручки:", round(profit_margin), "%")
    employee = int(input("Введите число сотрудников фирмы: "))
    proceeds_employee = proceeds / employee
    print("Один сотрудник принес фирме за месяц в среднем", round(proceeds_employee), "рублей от всей выручки")
elif proceeds == costs:
    print("Фирма работает в ноль.")
else:
    print(loss)
