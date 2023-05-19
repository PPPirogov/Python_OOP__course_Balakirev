def check(a):
    print(type(a))
    if type(a) in (int, float):
        return True
    else:
        raise ValueError("Неверный тип данных.")

check('3')