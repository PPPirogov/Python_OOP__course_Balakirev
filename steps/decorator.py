from datetime import datetime


def decor(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        a = func(*args, **kwargs)
        print(datetime.now() - start)
        return a
    return wrapper


@decor
def return_lst_long(n):
    # start = datetime.now()
    b = []
    for a in range(10 ** n):
        if a % 2 == 0:
            b.append(a)
    # print (datetime.now() - start)
    return b


@decor
def return_lst_short(n):
    # start = datetime.now()
    l = [x for x in range(10 ** n) if x % 2 == 0]
    # print (datetime.now() - start)
    return l


return_lst_long(8)
return_lst_short(8)
