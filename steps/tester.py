class SmartPhone:
    pass


class IPhone(SmartPhone):
    pass
print(issubclass(IPhone, SmartPhone))
print(issubclass(IPhone, object))
print(issubclass(SmartPhone, IPhone))
print(issubclass(SmartPhone, IPhone))
