class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, things=None):
        things = {} if things is None else things
        if things and not all(isinstance(key,Thing) for key in things):
            raise TypeError('можно передавать только целочисленные значения')
        super().__init__(things)

    def __setitem__(self, index, item):
        if type(index) == Thing:
            super().__setitem__(index, item)
        else:
            raise TypeError('можно передавать только целочисленные значения')


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2
print(*dict_things)

# for x in dict_things:
#     print(x.name)
#
# dict_things[1] = th_1 # исключение TypeError
