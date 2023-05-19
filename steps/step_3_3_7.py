class Complex:
    def __init__(self, real, img):
        self.check(real)
        self.check(img)
        self.__real = real
        self.__img = img
    @classmethod
    def check(cls,a):
        if type(a) in (int, float):
            return True
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if self.check(real):
            self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if self.check(img):
            self.__img = img

    def __abs__(self):
        return self.img*self.img+self.real*self.real


cm = Complex(7, 8)
cm.real = 3
cm.img = 4
c_abs = abs(cm)
#
# cm.img = 'sas'
print(abs(cm))
