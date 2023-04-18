class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, data):
        self.__data = data

    def __del__(self):
        return self

a = StackObj('dsdasd')
print(a.__dict__)