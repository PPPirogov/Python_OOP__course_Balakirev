class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y
    def get_coords(self):
        return (self.x,self.y)
pt = Point()
pt.set_coords(4,6)
print(pt.get_coords())
print(Point.__dict__)