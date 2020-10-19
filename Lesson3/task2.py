# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name: str = None,
              last_name: str = None,
              year: int = None,
              location: str = None,
              email: str = None,
              phone: int = None):
    return f'{name} {last_name}, {year} года рождения, проживает в городе {location}. Контакты: {phone}, {email}'


user_name = input("Пожалуйста, введите свое имя: ")
user_last_name = input("Введите свою фамилию: ")
user_year = int(input("Введите год рождения: "))
user_location = input("Введите город проживания: ")
user_email = input("Введите свою электронную почту: ")
user_phone = int(input("Введите номер телефона: "))

print(user_data(name=user_name, last_name=user_last_name, year=user_year, location=user_location, email=user_email, phone=user_phone))
