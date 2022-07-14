# Надо написать программу, которая из набора названий городов (все названия разные) строит цепочку максимальной длины.
# Запрещено повторять название городов.
# Города пользователь вводит одним действием в виде строки, где города разделены пробелами
class SomeClass:
    def __init__(self, cities,max_chain_length,avilable_cities):
        self.cities = cities
        self.max_chain_length = max_chain_length
        self.avilable_cities = avilable_cities
        self.rezult_chains = []
        self.all_chains = []
        self.used_cities = set()
        self.now_chain = []
        self.chain_city(self.cities,0)
        self.rezult_chains.append(self.get_max_chain())
    def chain_city(self,lst: list, id: int) -> list:


            if self.now_chain is None and self.used_cities is None:
                self.used_cities = set()
                self.now_chain = []
                self.all_chains = []
            start = lst[id]
            self.used_cities.add(start)
            self.now_chain.append(start)
            for i in range(len(lst)):
                if i == id:
                    continue
                if lst[i] not in self.used_cities and lst[i][0] == start[-1].upper():
                    self.chain_city(lst, i)
            self.all_chains.append(self.now_chain.copy())
            self.used_cities.remove(self.now_chain.pop())
            return max(self.all_chains, key=lambda x: len(x))

    def get_max_chain(self):
        return max(self.all_chains, key=lambda x: len(x))











