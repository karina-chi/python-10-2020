# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, _length, _width, _depth=5, _weight=25):
        self._length = _length
        self._width = _width
        self._depth = _depth
        self._weight = _weight

    def mass(self):
        return self._length * self._width * self._depth * self._weight


a = int(input("Введите длину дорожного полотна: "))
b = int(input("Введите ширину дорожного полотна: "))
r = Road(a, b)
print(f'{r.mass()} кг асфальта необходимо для покрытия дорожного полотна.')
