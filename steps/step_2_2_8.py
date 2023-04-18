class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        a = RadiusVector2D.MIN_COORD
        b = RadiusVector2D.MAX_COORD
        if a <= x <= b and a <= y <= b and type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            self.__x = self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in (int, float) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y

r3 = RadiusVector2D(3)
print(RadiusVector2D.norm2(r3))