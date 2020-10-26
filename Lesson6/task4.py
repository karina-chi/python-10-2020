# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name}: начало движения.')

    def stop(self):
        print(f'{self.name}: остановка.')

    def turn(self, direction: str):
        print(f'{self.name}: поворот на {direction}.')

    def show_speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость {self.name} выше разрешенной в городе.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость {self.name} выше разрешенной для рабочих машин.')


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(100, 'Red', 'Audi'),
    TownCar(60, 'White', 'Oka'),
    WorkCar(50, 'Rose', 'Lada'),
    PoliceCar(110, 'Blue',  'Ford')
]

cars[0].go()
cars[1].turn("лево")
cars[2].stop()
cars[3].turn("право")

for car in cars:
    car.show_speed()
