class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        #print("вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра" + str(self))


pt = Point(1, 2)
print(pt.__dict__)
