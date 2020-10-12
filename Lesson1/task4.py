# user_number = input("Введите целое положительное число: ")
# list(user_number)
# x = max(list(user_number))
# print(x)

user_number = input("Введите целое положительное число: ")
if not user_number.isdigit():
    print("Неверный формат числа.")
    exit()
number = int(user_number)
max_num = 0

while number and max_num != 9:
    current = number % 10
    number = number // 10
    max_num = current if current > max_num else max_num
print("Максимальное число: ", max_num)
