# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    size: int
    height: float

    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_fabric_cons_coat(self):
        return self.size / 6.5 + 0.5

    def get_fabric_cons_suit(self):
        return self.height * 2 + 0.3

    @property
    def get_fabric_consumption(self):
        return str(f'Суммарный расход ткани \n'
                   f' {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)} м.')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.fabric_cons_coat = round(self.size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход ткани на пальто {self.fabric_cons_coat} м.'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.fabric_cons_suit = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Расход ткани на костюм {self.fabric_cons_suit} м.'


coat = Coat(44, 1.65)
suit = Suit(44, 1.65)
print(coat)
print(suit)
print(coat.get_fabric_consumption)
print(suit.get_fabric_consumption)
print(coat.get_fabric_cons_coat())
print(suit.get_fabric_cons_suit())
