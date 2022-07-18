import abc   # Модуль abc содержит в себе абстрактные классы и методы.
from abc import ABC
import enum


class TaxSystem(ABC):
    def __init__(self, name, turnover, __str__, tax_calculation):
        self.name = name
        self.turnover = turnover
        self.tax_calculation = tax_calculation
        self.__str__ = __str__

    @abc.abstractmethod
    def tax_calculation(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
# Для создания абстракции необходимо создать класc, являющийся наследником класса abc.ABCMeta


class Fop(abc.ABC): # Для создания абстракции необходимо создать класc, являющийся наследником класса abc.ABCMeta
    def __init__(self, name, turnover, expenses, group):
        self.name = name
        self.turnover = turnover  # Прибыль предпринимателя  в квартале
        self.expenses = expenses  # Расходы предпринимателя в квартале
        self.group = group  # Группа предпринимателя

    @abc.abstractmethod
    def tax_calculation(self) -> float:
        pass

    def __str__(self) -> str:
        return f'{self.name}' + f' - {self.tax_calculation}'  # пишет имя предпринимателя и сумму налогов которую он должен заплатить за 1 квартал.


# single tax до 10% от прожиточного минимума раз на квартал, с 1 января 2022 года - 1430,0 (6500,0 х 22%)
class SingleTax(Fop):
    def tax_calculation(self) -> float:
        return self.turnover * 0.22


class Group(ABC):

    FOP_GROUP = 1
    FOP_GROUP_2 = 2
    FOP_GROUP_3 = 3

    def __init__(self, name, group):
        self.name = name
        self.group = group


class FopGroup(Fop, ABC):

    MAX_INCOME = 1085000    # 167 * 6500 максимальный доход предпринимателя это 167 размеров минимальных зарплат
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 248.10
    MINIMAL_SALARY = 6500
    # Минимальная зарплата предпринимателя

    def __init__(self, name: object, turnover: object, expenses: object, group: object) -> object:
        super().__init__(name, turnover, expenses, group)
        self.group = Group.FOP_GROUP
        self.group = Group.FOP_GROUP_2
        self.group = Group.FOP_GROUP_3

    def tax_calculation(self) -> float:
        if self.turnover > self.MAX_INCOME:  # Если прибыль предпринимателя больше максимального дохода
            return self.SSC, (self.MINIMAL_SALARY * 15) * 0.22  # (6500,0 х 15) х 22% = 21450 налог на прибыль
        else:
            Group.FOP_GROUP = Group.FOP_GROUP_2   # Переход на вторую группу предпринимателей


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
            Group.FOP_GROUP2 = Group.FOP_GROUP_3  # Переход на третью группу предпринимателей


class FopGroup3(Fop, ABC):

    MAX_INCOME = 7585500  # (1167 минималок) Максимальный доход предпринимателя
    SSC = 1430  # single social contribution  - сумма налога на прибыль от предпринимателя
    SINGLE_TAX = 1300.0
    MINIMAL_SALARY = 6500

    def __init__(self, name, turnover, expense, group):
        super().__init__(name, turnover, expense, group)

    def tax_calculation(self) -> float:
        if self.turnover > self.MAX_INCOME:
            return self.SSC, (self.MINIMAL_SALARY * 15) * 0.22
        pass


# В конце надо создать N ФОПов подать отчетность за них, и передaть их всех на подсчет налогов
FopGroup('ООО "Hive Five"', 167 * 6500, Group.FOP_GROUP)
FopGroup2('ООО "Twenty crazy fingers"', 834 * 6500, Group.FOP_GROUP_2)
FopGroup3('ООО "Предпринимательская группа"', 1167 * 6500, Group.FOP_GROUP_3)


# Создаем офис налогового инспектора и передаем ему всех ФОПов










