# Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов.
# При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса будут формироваться командой:
#
# line = LineTo(x, y)
# где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).
#
# В каждом объекте класса LineTo должны формироваться локальные атрибуты:
#
# x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).
#
# Объекты класса PathLines должны создаваться командами:
#
# p = PathLines()                   # начало маршрута из точки 0, 0
# p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
# где line1, line2, ... - объекты класса LineTo.
#
# Сам же класс PathLines должен иметь следующие методы:
#
# get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
# get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
# add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
#
# Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:
#
# L = sqrt((x1-x0)^2 + (y1-y0)^2)
#
# где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
import math
class PathLines:
    def __init__(self, *args):
        self.__args = args
        self.__all_path = [LineTo(0, 0)] + [lt for lt in args]
    def get_path(self):
        return self.__all_path[1:]

    def get_length(self):
        a = LineTo(0, 0)
        sum=0
        for i in self.__all_path[1:]:
            l = math.sqrt((i.x - a.x) ** 2 + (i.y - a.y) ** 2)
            sum+=l
            a = i

        return sum

    def add_line(self, line): #добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
        self.__all_path.append(line)


class LineTo:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []
