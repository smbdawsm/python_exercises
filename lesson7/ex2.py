'''Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся 
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, H = 0, V = 0):
        self.H = H
        self.V = V

    def __str__(self):
        if self.V != 0:
            return f'Площадь ткани на куртку {self.get_square}'
        else:
            return f'Площадь ткани на пиджак  {self.get_square}'
    @abstractmethod
    def get_square(self):
        pass

class Coat(Clothes):

    def __init__(self, V, H = 0):
        super().__init__(H)
        self.V = V
    
    @property
    def get_square(self):
        return (self.V*6.5 + 0.5)

class Costume(Clothes):

    def __init__(self, H, V = 0):
        super().__init__(V)
        self.H = H

    @property
    def get_square(self):
        return (2 * self.H + 0.3)

Jacket = Costume(1.8)
Coat1 = Coat(1)
print(Jacket)
print(Coat1)