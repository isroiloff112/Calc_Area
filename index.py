class Shape:
    def __init__(self):
        pass


class Parelellogram(Shape):
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.angle = 0

    def area(self):
        from math import sin, radians
        if self.angle == 0:
            self.angle = int(input("Enter angle between a and b sides: "))
            while self.angle >= 180 or self.angle < 0:
                print(
                    'The angle should not be equal or greater than 180 and negative number')
                self.angle = int(input('Please etry again: '))
            else:
                return self.a * self.b * sin(radians(self.angle))


class Rectangle(Parelellogram):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.angle = 90

    def area(self):
        return f'The area of rectangle is {self.a * self.b}'


class Rhombus(Parelellogram):
    def __init__(self, a):
        super().__init__(a, a)

    def area(self):
        from math import sin, radians
        if self.angle == 0:
            self.angle = int(input("Enter the angle of rhombus: "))
            while self.angle >= 180 or self.angle < 0:
                print(
                    'The angle should not be equal or greater than 180 and negative number')
                self.angle = int(input('Please etry again: '))
            else:
                return self.a * self.a * sin(radians(self.angle))


class Square(Rhombus):
    def __init__(self, a):
        super().__init__(a)
        self.angle = 90

    def area(self):
        return f'The area of square is {self.a * self.a}'


class Trapezium(Rhombus):
    def __init__(self, a):
        super().__init__(a)
        self.b = a * 0.5
        self.height = 0

    def calc_area(self):
        if self.height == 0:
            self.height = int(input("Enter the height of trapezium: "))
            while self.height <= 0:
                self.height = int(
                    input("Please enter a number greater than zero: "))
            return ((self.a + self.b)/2)*self.height


#p1 = Parelellogram(3, 4)
# print(p1.area())
#r1 = Rectangle(4,5)
# print(r1.area())
#r2 = Rhombus(2)
# print(r2.area())
#s1 = Square(4)
# print(s1.area())
t1 = Trapezium(8)
print(t1.calc_area())
