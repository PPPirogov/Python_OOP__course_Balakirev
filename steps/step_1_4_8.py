import sys


# здесь объявляется класс StreamData
class StreamData:

    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            for a in range(len(fields)):
                setattr(self, fields[a], lst_values[a])
            print(self.__dict__)
            return True



class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = [
            '10',
            'Питон - основы мастерства',
            '512'
        ]#list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(result)
print(data.__dict__)
