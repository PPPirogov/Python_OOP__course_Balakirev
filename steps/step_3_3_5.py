class WordString:
    def __init__(self, string=''):
        self.__string = string
    @property
    def string(self):
        return self.__string
    @string.setter
    def string(self,string):
        self.__string = string

    def __len__(self):
        a = len(self.__string.split())
        return a
    def __call__(self, indx):
        l = self.__string.split()
        return l[indx]

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
print(n)
print(words.string)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")