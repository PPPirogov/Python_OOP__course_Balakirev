class A:
    def __del__(self):
        return print(self)

b = A()