import math


class RadiusVector:
    def __init__(self, arg,*args):
        if len(args) == 0:
            self.__args = [0] * arg
        else:
            self.__args = [arg]+list(args)

    def set_coords(self, *args):
        n = min(len(self.__args), len(args))
        self.__args[:n] = args[:n]

    def get_coords(self):
        return tuple(self.__args)

    def __len__(self):
        return len(self.__args)

    def __abs__(self):
        a = 0
        for i in self.__args:
            a += i * i
        return math.sqrt(a)


vector3D = RadiusVector(3)
print(vector3D.__dict__)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.__dict__)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.__dict__)
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
print(vector3D.__dict__)
print(res_len)
res_abs = abs(vector3D)
print(res_abs)
v4D = RadiusVector(4)
print(v4D.__dict__)
v4D.set_coords(10, 20, 30, 40)
print(v4D.__dict__)
