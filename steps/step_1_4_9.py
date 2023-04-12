import sys

# программу не менять, только добавить два метода
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):
        d = []
        while a <= b:
            try:
                d.append(self.lst_data[a])
            except:
                pass
            a+=1
        return d

    def insert(self, data):
        for a in data:
            b = a.split(' ')
            c = {}
            for a in range(len(self.FIELDS)):
                c[self.FIELDS[a]] = b[a]
            #c = {self.FIELDS[0]: b[0], self.FIELDS[1]: b[1], self.FIELDS[2]: b[2], self.FIELDS[3]: b[3]}
            self.lst_data.append(c)
        #print(self.lst_data)


db = DataBase()
db.insert(lst_in)
print(db.select(1, 50))
