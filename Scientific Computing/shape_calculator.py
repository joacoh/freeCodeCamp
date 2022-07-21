class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if (self.width>50 or self.height>50):
            return 'Too big for picture.'
        else:
            side = ('*'*self.width + '\n')*self.height
            return side

    def get_amount_inside(self, shape):
        return int(self.get_area()/shape.get_area())

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return 'Square(side={})'.format(self.width)

    def set_side(self, side):
        self.width = side
        self.height = side       

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)