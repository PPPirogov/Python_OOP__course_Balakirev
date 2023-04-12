"""
Объявите три класса геометрических фигур: Line, Rect, Ellipse.
Должна быть возможность создавать объекты каждого класса следующими командами:
g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа).
В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.
Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse).
Координаты также генерируются случайным образом (числовые значения).
Все объекты сохраните в списке elements.
В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
"""
import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = [a, b]
        self.ep = [c, d]


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = [a, b]
        self.ep = [c, d]


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = [a, b]
        self.ep = [c, d]


elements = []
for a in range(217):
    elements.append(random.choice([Line(random.random(), random.random(), random.random(), random.random()),
                                   Rect(random.random(), random.random(), random.random(), random.random()),
                                   Ellipse(random.random(), random.random(), random.random(), random.random())]
                                  ))
# print(elements)

for a in elements:
    #print(type(a))
    if type(a) == "<class '__main__.Line'>":
        print(type(a))
        #a.sp = [0, 0]
        #a.ep = [0, 0]
# a = Line(random.random(), random.random(), random.random(), random.random())
# print(a.ep, a.sp)
