class Clock:
    __DAY = 84600  # число секунд в однном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целочисленным числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24

        return f"{self.__get_fromatted(h)}:{self.__get_fromatted(m)}:{self.__get_fromatted(s)}"

    @classmethod
    def __get_fromatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        sc = other
        if isinstance(other,Clock):
            sc = other.seconds
        self.seconds+=sc
        return self

c1 = Clock(32130321)
c2 = Clock(31233)
c3 = Clock(3233)
c1 += c2
print(c1.get_time())
