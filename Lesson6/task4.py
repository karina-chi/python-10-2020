# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name}: начало движения.'

    def stop(self):
        return f'{self.name}: остановка.'

    def turn_right(self):
        return f'{self.name}: поворот на право.'

    def turn_left(self):
        return f'{self.name}: поворот на лево.'

    def show_speed(self):
        return f'Текущая скорость {self.name} равна {self.speed} км/ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} равна {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной в городе.'
        else:
            return f'Скорость {self.name} соответствует разрешенной в городе.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} равна {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной для рабочих машин.'
        else:
            return f'Скорость {self.name} соответствует разрешенной для рабочих машин.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина.'
        else:
            return f'{self.name} - не полицейская машина.'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(60, 'White', 'Oka', False)
lada = WorkCar(50, 'Rose', 'Lada', False)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.go())
print(f'{oka.turn_right()}, {audi.stop()}')
print(f'{ford.name} {ford.color}')
print(f'{audi.name} - полицейская машина? {audi.is_police}')
print(f'{oka.name} - полицейская машина? {oka.is_police}')
print(audi.show_speed())
print(lada.show_speed())
print(ford.police())
print(ford.show_speed())
