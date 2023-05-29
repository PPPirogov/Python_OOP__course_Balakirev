class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __len__(self):
        return len(self.coords)
    def get_coords(self):
        return tuple(self.coords)

    def __add__(self, other):
        if len(self.coords) == len(other):
            p = tuple(a + b for a,b in zip(self.coords,other.get_coords()))
            print(p)
            return Vector(p)
        else:
            raise TypeError('размерности векторов не совпадают')

    def __sub__(self, other):
        if len(self.coords) == len(other):
            p = tuple([self.coords[x] + other.coords[x] for x in range(len(self.coords))])

            c="#".join(p)
            print(c)
            return Vector(c)
        else:
            raise TypeError('размерности векторов не совпадают')


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
print(*v1.coords)
print(len(v1))
v = v1 + v2
print(v.__dict__)
print(v1.__dict__)