class ObjList:
    def __int__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, a):
        self.__prev = a

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, a):
        self.__next = a

    def __new__(cls, *args, **kwargs):
        cls.obj = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(obj):
        pass
    # добавление нового объекта obj класса ObjList в конец связного списка;
    def remove_obj(indx):
        pass
    # удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.
    def __len__(self):
        a = len(self.__string.split())
        return a

    def linked_lst(indx):
        return

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))