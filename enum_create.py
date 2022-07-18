import abc   # Модуль abc содержит в себе абстрактные классы и методы.
import enum
from abc import ABC


class Group_Fop (enum.Enum):
    FOP_GROUP = 1
    FOP_GROUP_2 = 2
    FOP_GROUP_3 = 3

# Для создания абстракции необходимо создать класc, являющийся наследником класса abc.ABC
class Fop(abc.ABC):  # Для создания абстракции необходимо создать класc, являющийся наследником класса abc.ABCMeta
    def __init__(self, name, turnover, expenses, group):
        self.name = name
        self.turnover = turnover  # Прибыль предпринимателя  в квартале
        self.expenses = expenses  # Расходы предпринимателя в квартале
        self.group = group  # Группа предпринимателя
        self.group = Group_Fop.FOP_GROUP
        self.group = Group_Fop.FOP_GROUP_2
        self.group = Group_Fop.FOP_GROUP_3

# single tax до 10% от прожиточного минимума раз на квартал, с 1 января 2022 года - 1430,0 (6500,0 х 22%)

class FopGroup(Fop, ABC):

    MAX_INCOME = 1085000    # 167 * 6500 максимальный доход предпринимателя это 167 размеров минимальных зарплат
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 248.10
    MINIMAL_SALARY = 6500

    def __init__(self, name, turnover, expenses, group):
        super().__init__(name, turnover, expenses, group)
        self.group = Group_Fop.FOP_GROUP
        self.group = Group_Fop.FOP_GROUP_2
        self.group = Group_Fop.FOP_GROUP_3

    def tax_calculation(self) -> float:
        if self.turnover > self.MAX_INCOME:  # Если прибыль предпринимателя больше максимального дохода
            return self.SSC, (self.MINIMAL_SALARY * 15) * 0.22  # (6500,0 х 15) х 22% = 21450 налог на прибыль
        else:
            Group_Fop.FOP_GROUP = Group_Fop.FOP_GROUP_2   # Переход на вторую группу предпринимателей


class FopGroup2(Fop, ABC):

    MAX_INCOME = 5421000  # (834 минималки)
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 1300.0
    MINIMAL_SALARY = 6500

    def __init__(self, name, turnover, group):
        super().__init__(name, turnover, group)

    def tax_calculation(self) -> float:
        if self.turnover > self.MAX_INCOME:
            return self.SSC, (self.MINIMAL_SALARY * 15) * 0.22
        else:
            Group_Fop.FOP_GROUP2 = Group_Fop.FOP_GROUP_3  # Переход на третью группу предпринимателей


class FopGroup3(Fop, ABC): # Класс FopGroup3 наследует класс Fop

    MAX_INCOME = 7585500  # (1167 минималок) Максимальный доход предпринимателя
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 1300.0
    MINIMAL_SALARY = 6500

    def __init__(self, name: object, turnover: object, expenses: object, group: object) -> object:
        super().__init__(name, turnover, expenses, group)

    def tax_calculation(self) -> float:
        if self.turnover > self.MAX_INCOME:
            return self.SSC, (self.MINIMAL_SALARY * 15) * 0.22
        pass


# В конце надо создать N ФОПов подать отчетность за них,

#  и передать их всех на подсчет налогов и получить отчет

class TaxInspector(ABC) :
    def __init__(self, fop):
        self.fop = fop

    def tax_calculation(self, fop):
        pass

        if isinstance(fop, FopGroup):
            return fop.tax_calculation()
        elif isinstance(fop, FopGroup2):
            return fop.tax_calculation()
        elif isinstance(fop, FopGroup3):
            return fop.tax_calculation()
        else:
            return "Неизвестный класс"

FOP_Tiger = Fop("Tiger", 75810, 2334, Group_Fop.FOP_GROUP)
FOP_Sandman = Fop("Sandman", 33310, 25554, Group_Fop.FOP_GROUP_3)
FOP_Lion = Fop("Lion", 54310, 3454, Group_Fop.FOP_GROUP)
FOP_Tiger2 = Fop("Tiger", 75810, 2334, Group_Fop.FOP_GROUP_2)


print(TaxInspector(FOP_Tiger).tax_calculation(FOP_Tiger))
print(TaxInspector(FOP_Sandman).tax_calculation(FOP_Sandman))
print(TaxInspector(FOP_Lion).tax_calculation(FOP_Lion))
print(TaxInspector(FOP_Tiger2).tax_calculation(FOP_Tiger2))























