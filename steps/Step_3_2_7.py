#  Предположим, вам необходимо создать программу по преобразованию списка строк, например:
#
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить не нужно):
#
# '''<ul>
# <li>Пункт меню 1</li>
# <li>Пункт меню 2</li>
# <li>Пункт меню 3</li>
# </ul>'''
#
# Для этого необходимо объявить класс RenderList, объекты которого создаются командой:
#
# render = RenderList(type_list)
# где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>). Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.
#
# Затем, предполагается использовать объект render следующим образом:
#
# html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
# Пример использования класса (эти строчки в программе писать не нужно):
#
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# render = RenderList("ol")
# html = render(lst)
class RenderList:
    def __init__(self, type_list):
        if type_list == "ol":
            self.type_list= type_list
        else:
            self.type_list = "ul"
    def __call__(self,lst, *args, **kwargs):
        answer = f'<{self.type_list}>\n'
        for a in lst:
            answer+=f'<li>{a}</li>\n'
        answer += f'</{self.type_list}>'
        return answer

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
print(render.__dict__)
html = render(lst)
print(html)