# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, last_name, year, location, email, phone):
    print(f'{name} {last_name}, {year} года рождения, проживает в городе {location}. Контакты: {phone}, {email}')


name = input("Пожалуйста, введите свое имя: ")
last_name = input("Введите свою фамилию: ")
year = input("Введите год рождения: ")
location = input("Введите город проживания: ")
email = input("Введите свою электронную почту: ")
phone = input("Введите номер телефона: ")

user_data(name=name, last_name=last_name, year=year, location=location, email=email, phone=phone)
