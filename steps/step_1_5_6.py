"""
Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.
В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.
Проверку параметров a, b, c проводить именно в таком порядке.
Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c.
Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
Sample Input:
3 4 5
Sample Output:
3
"""


#
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.d = [a, b, c]
#
#     def is_triangle(self):
#         for a in self.d:
#             if a <= 0:
#                 return 1
#             if isinstance(a, int):
#                 pass
#             else:
#                 if isinstance(a, float):
#                     pass
#                 else:
#                     return 1
#         if ((self.d[0] > self.d[1] + self.d[2]) or (self.d[1] > self.d[0] + self.d[2]) or (self.d[2] > self.d[0] + self.d[0])):
#             return 2
#         else :
#             return 3
#
# tr = TriangleChecker(3, 6, 5)
# print(tr.is_triangle())

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1
        a,b,c =self.a,self.b,self.c
        if a >= b + c or b >= a + c or c >= a + b:
            return 2
        return 3


tr = TriangleChecker(3, 9, 12)
print(tr.is_triangle())
