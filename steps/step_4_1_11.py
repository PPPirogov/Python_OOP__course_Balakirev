class Vector:
    _allowed_types = (int, float)

    def __init__(self, *coords):
        self.__ckeck_coords(coords)
        self.coords = coords

    def __ckeck_coords(self,coords):
        print(self)
        print (self._allowed_types)
        if not all(type(x) in self._allowed_types for x in coords):
            ValueError('Неверный тип координат')

    def __len__(self):
        return len(self.coords)

    def get_coords(self):
        return tuple(self.coords)

    def __add__(self, other):
        if len(self.coords) == len(other):
            p = tuple(a + b for a, b in zip(self.coords, other.get_coords()))
            return Vector(*p)
        else:
            raise TypeError('размерности векторов не совпадают')

    def __sub__(self, other):
        if len(self.coords) == len(other):
            p = tuple(a - b for a, b in zip(self.coords, other.get_coords()))
            return self.__class__(*p)
        else:
            raise TypeError('размерности векторов не совпадают')

class VectorInt(Vector):
    _allowed_types = (int,)

v1 = VectorInt(1, 0.5, 3)
# print(v1)
v2 = VectorInt(3, 4, 5)
v4 = VectorInt(5, 1, 3)
# print(*v1.coords)
# print(len(v1))
v = v1 - v2
v3= v4 + v2
# print(v.__dict__, v)
# print(v3.__dict__, v3)
