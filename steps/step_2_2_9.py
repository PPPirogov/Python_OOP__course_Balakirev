class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    @classmethod
    def predict(cls, root, x):  # def predict(cls, root, x) - для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root.
        b = root
        d = ''
        # for a in x:
        #     if a == 1:
        #         #print(b.left.value)
        #         b=b.left
        #         d = b.left.value
        #     elif a == 0:
        #         b = b.right
        #         #print(b.right.value)
        #         d = b.right.value
        #     #print(f' a = {a}    value = {b.value}')
        while b.value == None:
            if x[b.indx]==1:
                b = b.left
            else:
                b = b.right

        return b.value


    @classmethod
    def add_obj(cls, obj, node=None,left=True):  # для добавления вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj);
        if node != None:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

# print(f'{root} : {root.__dict__}')
# print(f'{v_11} : {v_11.__dict__}')
# print(f'{v_12} : {v_12.__dict__}')
# print(DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11).__dict__)

# x = [1, 1, 0]
# res = DecisionTree.predict(root, x)
# print(res)

y = [0, 1, 1]
res = DecisionTree.predict(root, y)
print(res)