# user_number = input("Введите целое положительное число: ")
# list(user_number)
# x = max(list(user_number))
# print(x)

user_number = int(input("Введите целое положительное число: "))
lst = []
while user_number > 10:
    lst.append(user_number % 10)
    user_number = user_number // 10
r = max(lst)
print(r)
