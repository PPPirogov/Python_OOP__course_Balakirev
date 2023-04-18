class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data




class Stack:
    top = None



    def push(self, obj):
        if self.top == None:
            self.top = obj

        else:
            object = self.top
            while object.next != None:
                object = object.next
            object.next = obj
            # print(object.next)

    def pop(self):
        object = self.top
        prev= None
        if object != None:
            while object.next != None:
                prev = object
                object = object.next
            if prev != None:
                prev.next = None
                #self.top = None
            else:
                a = self.top
                self.top = None
                return a

        return object

    def get_data(self):
        lst = []
        object = self.top
        if object != None:
            lst.append(object.data)
            while object.next != None:
                object = object.next
                lst.append(object.data)

        return lst

# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления, или пустой список, если объектов нет).
#
# Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):


# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# #print(Stack.top.data)
# st.pop()
# res = st.get_data()  # ['obj1', 'obj2']
# #print(res)

st = Stack()
for i in range(20):
    st.push(StackObj(f'Первые данные {i}'))

print(st.get_data(), end='\n\n')

for i in range(10):
    st.pop()

print(st.get_data(), end='\n\n')

for i in range(10):
    st.push(StackObj(f'Вторые данные {i}'))

print(st.get_data(), end='\n\n')

for i in range(20):
    st.pop()

print(st.get_data(), end='\n\n')

for i in range(10):
    st.pop()

print(st.get_data(), end='\n\n')

for i in range(10):
    st.push(StackObj(f'Третьи данные {i}'))

print(st.get_data(), end='\n\n')

for i in range(5):
    st.pop()

print(st.get_data(), end='\n\n')