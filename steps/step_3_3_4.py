class Model:
    def __init__(self):
        self.lst = {}

    def query(self, **kwargs):
        self.lst = kwargs

    def __str__(self):
        a = 'Model: '
        for b in self.lst:
            a += f'{b} = {self.lst[b]}, '
        if a == 'Model: ':
            a = 'Model'
        else:
            a = a[:-2]

        return f'{a}'

    # def __repr__(self):
    #     return "Model"


model = Model()
#model.query(id=1, fio='Sergey', old=33)
print(model)
