# Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса:
# при создании экземпляров должно возвращаться значение None, например:
#
# em = EmailValidator() # None
# В самом классе реализовать следующие методы класса (@classmethod):
#
# get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
# check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.
#
# Корректность строки email определяется по следующим критериям:
#
# - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать 100 (сто включительно);
# - длина email после символа @ не должна быть больше 50 (включительно);
# - после символа @ обязательно должна идти хотя бы одна точка;
# - не должно быть двух точек подряд.
#
# Также в классе нужно реализовать приватный статический метод класса:
#
# is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.
#
# Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.
#
# Пример использования класса EmailValidator (эти строчки в программе писать не нужно):
#
# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False
import random
from string import ascii_lowercase, digits
import re
from accessify import private
class EmailValidator:
    def __new__(cls,*args,**kwargs):
        return None

    @classmethod
    def get_random_email(cls): #для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
        email_name = random.randint(1, 100)
        CHARS = ascii_lowercase + '_.'
        CHARS_CORRECT = CHARS + CHARS.upper() + digits
        email = ''.join(
            random.choice(CHARS_CORRECT) for _ in
            range(email_name)) + '@gmail.com'
        return email

    @classmethod
    def check_email(cls, email):
        if EmailValidator.__is_email_str(email):
            pattern = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
            match = re.fullmatch(pattern, email)
            if match == None:
                return False
            else:
                return True
        else:
            return False



    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        else:
            return False

print (EmailValidator.get_random_email())

print (EmailValidator.check_email('QUf@gmail.c.om'))


