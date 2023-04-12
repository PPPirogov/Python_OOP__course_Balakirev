class Person:
    name= 'Сергей Балакирев'
    job= 'Программист'
    city= 'Москва'
p1 = Person()
print(hasattr('p1','job'))
print(hasattr(Person,'job'))
print('job' in p1.__dict__)