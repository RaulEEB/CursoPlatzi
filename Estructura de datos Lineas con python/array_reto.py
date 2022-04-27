import random

class Array_Reto:

    def __init__(self, capacity,fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __string__(self):
        return str(self.items)

    def __populate__(self):
        for i in range(self.__len__()):
            self.items[i] = random.randint(0,100)

    def total(self):
        totales = 0
        for i in range(self.__len__()):
            totales += self.items[i]
        return totales

if __name__ == '__main__':
    array_reto = Array_Reto(10)
    array_reto.__populate__()
    print(array_reto.__string__())
    print(array_reto.total())
    