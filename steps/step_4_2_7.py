class Tuple(tuple):
    def __init__(self,iter_obj=None):
        super().__init__()
    def __add__(self, other):
        return Tuple(super().__add__(tuple(other)))

t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
a = "Python"
print(tuple(a))