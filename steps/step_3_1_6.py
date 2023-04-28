class Course:
    def __init__(self, name):
        self.name = name
        self.modules=[]

    def add_module(self, module):
        self.modules.append(module)
    def remove_module(self, indx):
        self.modules.pop(indx)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title':
            if type(value) != str:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'practices':
            if type(value) not in (int, float) and value >= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'duration':
            if type(value) not in (int, float) and value >= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ('title', 'practices', 'duration'):
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
        object.__delattr__(self, item)

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)