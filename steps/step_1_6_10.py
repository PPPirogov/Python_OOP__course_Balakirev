class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        Point(self.x, self.y)
        return Point(self.x, self.y)


pt = Point(3, 5)
pt_clone = pt.clone()
