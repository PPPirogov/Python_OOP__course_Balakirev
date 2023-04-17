class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):  # добавление нового объекта obj класса ObjList в конец связного списка;
        if self.tail==None:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):  # даление последнего объекта из связного списка;
        if self.tail.get_prev() != None:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.head = None

    def get_data(self):  # получение списка из строк локального свойства __data всех объектов связного списка.
        a = self.head
        answer = []
        #print (a)
        #print(a.get_data())
        #print(a.get_next())
        while a != None:
            #print(a.get_data())
            answer.append(a.get_data())
            a=a.get_next()
        return answer

class ObjList:
    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def set_next(self, obj):  # - изменение приватного свойства __next на значение obj;
        self.__next = obj

    def set_prev(self, obj):  # - изменение приватного свойства __prev на значение obj;
        self.__prev = obj

    def set_data(self, data):  # - изменение приватного свойства __data на значение data;
        self.__data = data

    def get_next(self):  # - получение значения приватного свойства __next;
        return self.__next

    def get_prev(self):  # - получение значения приватного свойства __prev;
        return self.__prev

    def get_data(self):  # - получение значения приватного свойства __data.
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
#print(res)
lst.remove_obj()
lst.remove_obj()
lst.remove_obj()
abc = lst.get_data()
print(abc)