# Вам необходимо в программе объявить классы валидаторов:
#
# LengthValidator - для проверки длины данных в диапазоне [min_length; max_length];
# CharsValidator - для проверки допустимых символов в строке.
#
# Объекты этих классов должны создаваться командами:
#
# lv = LengthValidator(min_length, max_length) # min_length - минимально допустимая длина; max_length - максимально допустимая длина
# cv = CharsValidator(chars) # chars - строка из допустимых символов
# Для проверки корректности данных каждый валидатор должен вызываться как функция:
#
# res = lv(string)
# res = cv(string)
# и возвращать True, если string удовлетворяет условиям валидатора и False - в противном случае.
#
# P.S. В программе следует только объявить два класса валидаторов, на экран выводить ничего не нужно.
class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
    def __call__(self,string, *args, **kwargs):
        return self.min_length <= len(string) <= self.max_length

class CharsValidator:
    def __init__(self,chars):
        self.chars=chars # chars - строка из допустимых символов
    def __call__(self,string, *args, **kwargs):
        list_string = list(string)
        list_chars = list(self.chars)
        for a in list_string:
            if a not in list_chars:
                return False
        return True
