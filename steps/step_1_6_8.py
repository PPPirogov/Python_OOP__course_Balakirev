class SingletonFive:
    counter = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.counter < 5:
            cls.__instance = super().__new__(cls)
        cls.counter += 1
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
for a in objs:
    print(a.name)