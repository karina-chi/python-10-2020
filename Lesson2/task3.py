# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите месяц в виде целого числа от 1 до 12: "))

winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]

if month in winter_list:
    print("Это зимний месяц.")
elif month in spring_list:
    print("Это весенний месяц.")
elif month in summer_list:
    print("Это летний месяц.")
else:
    print("Это осенний месяц.")

month_2 = int(input("Введите месяц в виде целого числа от 1 до 12: "))
seasons_dict = {
    "зима":[12, 1, 2],
    "весна":[3, 4, 5],
    "лето":[6, 7, 8],
    "осень":[9, 10, 11]
}
for seasons, months in seasons_dict.items():
    if month_2 in months:
        print(f'Время года - {seasons}.')
