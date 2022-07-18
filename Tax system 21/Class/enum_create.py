import enum  # Модуль enum содержит в себе тип для перечисления значений, с возможностью итерирования.
import abc   # Модуль abc содержит в себе абстрактные классы и методы.
from abc import ABC


class Group(enum.Enum):  # Для создания перечисления необходимо создать класc, являющийся наследником класса enum.Enum

    FOP_GROUP = 1
    FOP_GROUP_2 = 2
    FOP_GROUP_3 = 3


# Для создания абстракции необходимо создать класc, являющийся наследником класса abc.ABCMeta
class Fop(abc.ABC): # Для создания абстракции необходимо создать класc, являющийся наследником класса abc.ABCMeta
    def __init__(self, name, turnover, expenses, group):
        self.name = name
        self.turnover = turnover  # Прибыль предпринимателя
        self.expenses = expenses  # Расходы предпринимателя
        self.group = group  # Группа предпринимателя

    def tax_return(self) -> float:
        return self.turnover - self.expenses


    @abc.abstractmethod
    def tax_calculation(self) -> float:
        pass


    def __str__(self) -> str:
        return f'{self.name}' + f' - {self.tax_calculation()}'


# single tax до 10% от прожиточного минимума раз на квартал, с 1 января 2022 года - 1430,0 (6500,0 х 22%)
class SingleTax(Fop):
    def tax_calculation(self) -> float:
        return self.turnover * 0.22


class FopGroup1(Fop, ABC):

    MAX_INCOME = 1085000    # 167 * 6500 максимальный доход предпринимателя это 167 размеров минимальных зарплат
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 248.10
     # Минимальная зарплата предпринимателя

    def __init__(self, name, turnover, expenses, group):
        super().__init__(name, turnover, expenses, group)    # Вызов конструктора класса Fop

    def tax_calculation(self) -> float:
        if self.turnover > self.MAX_INCOME:  # Если прибыль предпринимателя больше максимального дохода
            return self.SSC,(self.MINIMAL_SALARY * 15) * 0.22  # (6500,0 х 15) х 22% = 21450 налог на прибыль


class FopGroup2(Fop, ABC):

    MAX_INCOME = 5421000  # (834 минималки)
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 1300.0
    MINIMAL_SALARY = 6500

    def __init__(self, name, turnover, expenses, group):
        super().__init__(name, turnover, expenses, group)   # Вызов конструктора класса Fop






class FopGroup3(Fop):

    MAX_INCOME = 7585500  # (1167 минималок)
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 1300.0
    MINIMAL_SALARY = 6500

    def tax_calculation(self) -> float:
        if self.group == Group.FOP_GROUP:
            return self.turnover * 0.05
