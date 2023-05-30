# Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:
#
# __init__()
# __setitem__()
# append()
#
# так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, генерировать исключение командой:
#
# raise TypeError('можно передавать только целочисленные значения')
# Пример использования класса ListInteger (эти строчки в программе не писать):
#
# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# s[0] = 10.5 # TypeError
# P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.

class ListInteger(list):

    def check(self, lst):
        if not all(type(x) == int for x in lst):
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, iterable):
        self.check(iterable)
        super().__init__(iterable)

    def __setitem__(self, index, item):
        if type(item) == int:
            super().__setitem__(index, item)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def append(self, item):
        if type(item) == int:
            super().append(item)
        else:
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 36))
print(s)
s[1] = 10
print(s)
s.append(11)
print(s)
s[0] = 10.5
