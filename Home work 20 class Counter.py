
"""
Self - это объект класса в котором вызывается метод. В задаче это будет счетчик
__init__ инициализирует объект класса и передает параметры в конструктор класса в виде ключевого слова self и параметров
"""


class Counter:
    # установка максимального и минимального значений (так же начального значения счётчика)
    def __init__(self, min_value, max_value) -> None:  # по умолчанию возврщает None
        self.min_value = min_value
        self.max_value = max_value
        self.counter = min_value

    # при инициализации увеличения счетчика на 1 возвращения текущего значения счётчика
    def increase(self):
        if self.counter < self.max_value:
            self.counter += 1
            return self.counter

    # методы сравнения и равенства двух счетчиков

    def __eq__(self, other):
        return self.counter == other.counter     # метод сравнения двух счетчиков

    def __ne__(self, other):
        return self.counter != other.counter     # метод равенства двух счетчиков

