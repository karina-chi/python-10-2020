user_answer = int(input("Введите время в секундах: "))
second = 60
minute = 60
hour = minute * second
hours = user_answer / hour
minutes = (hours - int(hours)) * second
seconds = user_answer - (int(hours) * hour + int(minutes) * second)
if hours >= 1:
    print(int(hours), ":", int(minutes), ":", seconds)
else:
    print("00", ":", minutes, ":", seconds)
