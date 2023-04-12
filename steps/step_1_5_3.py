class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y


points = []

for a in range(1000):
    print(a)
    if a == 1:
        print('HI')
        b = Point(2 * a + 1, 2 * a + 1, 'yellow')
        print(b.__dict__)
        print(Point.__dict__)
        points.append(b)
    else:
        b = Point(2 * a + 1, 2 * a + 1)
        print(b.__dict__)
        print(Point.__dict__)
        points.append(b)

#print(points)