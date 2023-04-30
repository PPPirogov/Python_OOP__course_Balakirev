import time
def check(data):
    if type(data) in (int, float) and data > 0:
        return True
    else:
        return False


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = [None, None, None]

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and type(filter) == Mechanical and self.slots[0] == None:
            self.slots[0] = filter
        elif slot_num == 2 and type(filter) == Aragon and self.slots[1] == None:
            self.slots[1] = filter
        elif slot_num == 3 and type(filter) == Calcium and self.slots[2] == None:
            self.slots[2] = filter
        # self.slots[slot_num-1]=filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return self.slots

    def water_on(self):
        a = time.time() - self.slots[0].date
        b = time.time() - self.slots[0].date
        c = time.time() - self.slots[0].date
        if None not in self.slots and 0 <= a <= self.MAX_DATE_FILTER and 0 <= b <= self.MAX_DATE_FILTER and 0 <= c <= self.MAX_DATE_FILTER:
            return True
        else:
            False

class Mechanical:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.data

    def __setattr__(self, key, value):
        try:
            self.data
            return
        except AttributeError:
            if key == 'data' and not check(value):
                return
        object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, data):
        self.data = data
    @property
    def data(self):
        return self.data
    def __setattr__(self, key, value):
        try:
            self.data
            return
        except AttributeError:
            if key == 'data' and not check(value):
                return
        object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.data

    def __setattr__(self, key, value):
        try:
            self.data
            return
        except AttributeError:
            if key == 'data' and not check(value):
                return
        object.__setattr__(self, key, value)

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
# w = my_water.water_on() # False
# my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on() # True
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
