# С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример, объявите в программе класс с именем:
#
# Singleton
#
# который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). Как это делать, вы должны уже знать из этого курса.
#
# Затем, объявите еще один класс с именем:
#
# Game
#
# который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:
#
# game = Game(name)
# где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим содержимым.
#
# Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).
#
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        print(cls)
        print(Singleton._instance)
        print(cls._instance)
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        super().__init__()
        if 'name' not in self.__dict__:
            self.name = name
class Game2(Singleton):
    def __init__(self, name):
        super().__init__()
        if 'name' not in self.__dict__:
            self.name = name

sin1 = Singleton()
game1 = Game('hi')
game2 = Game2('hi2')
game23 = Game2('hi2')
# print(game1.__dict__)
# print(game2.__dict__)
sin = Singleton()
