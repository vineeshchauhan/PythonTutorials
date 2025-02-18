#Numbers
#Strings
#Boolean
#Lists
#Dictionaries

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f'Move by {self.x}')

    def draw(self):
        print('Draw')


point1 = Point(10, 2)
point1.x = 10
point1.y = 20
point1.draw()
point1.move()
print(point1.x)

point2 = Point(2, 3)
