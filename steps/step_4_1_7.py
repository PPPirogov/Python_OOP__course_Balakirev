class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request, method):
        if method.upper() not in (self.methods):
            raise TypeError('данный запрос не может быть выполнен')
        else:
            f = getattr(self,method.lower(),False)
            if f:
                return f(request)
    def get(self,request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        else:
            if 'url' not in request.keys():
                raise TypeError('request не содержит обязательного ключа url')
            else:
                return f"url: {request['url']}"


dv1 = DetailView()  # по умолчанию methods=('GET',)
dv2 = DetailView(methods=('PUT', 'POST'))
print(dv1.__dict__)
print(dv2.__dict__)
dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')