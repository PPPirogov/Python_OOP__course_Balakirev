class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst,other_list))

    @staticmethod
    def __diff_list(lst_1,lst_2):
        if len(lst_2)==0
            return lst_1
        sub = lst_2[:]
        return[x for x in lst_1 if not NewList.__is_elem(x,sub)]
        # if isinstance(other, NewList):
        #     sc = other.args

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        sc = other
        if isinstance(other, NewList):
            sc = other.args
        # self.args-=sc
        return self


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
# print(lst1.get_list())
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
