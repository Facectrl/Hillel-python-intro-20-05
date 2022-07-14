import enum   #   Перчечисление для определения типа пути для поиска пути


class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class DriveType(enum.Enum):

    full_DRIVE = 0
    BACK_DRIVE = 1
    FRONT_DRIVE = 2

class Gasstation:

    def __init__(self, name,x,y, color):
        self.name = name
        self.x = x
        self.y = y
        self.color = color

class Car:

    def __init__(self,model: str,color: str,year: int,drive_type=DriveType.full) -> None:  # конструктор класса Car с аргументами model, color, year
        self.model = model
        self.color = color    
        self.year = year


red_car = Car("BMW","RED",2020)  # Создание объекта класса Car
green_car = Car("Audi","GREEN",2019)  # Создание объекта класса Car
blue_car = Car("Mercedes","BLUE",2018)


print(red_car)
print(green_car)
print(blue_car)
print(isinstance(red_car, Car))

__dict__ = {}    # поле для хранения атрибутов класса в виде словаря  для получения доступа к атрибутам класса

# проверка на тип объекта red_car
print(f"red_car is instance of Car: {isinstance(red_car, Car)}")  # проверка на тип объекта red_car