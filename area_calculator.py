from math import pi, sqrt


class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        # This function returns the area of the shape
        return self.side1 * self.side2

    def __str__(self):
        # It allows you to modify the way an instance will print.
        return f"The area of {self.__class__.__name__} is {self.get_area():,.2f}"
        # The self.__class__.__name__ hidden attribute refers to the name of the class.
        # If you were working with a Triangle class, that attribute would be “Triangle.”


class Rectangle(Shape):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(side1=base, side2=height)

    def get_area(self):
        # A method defined in the superclass is called and the result is stored as a variable
        area = super().get_area()
        return area / 2


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(side1=radius, side2=radius)

    def get_area(self):
        return pi * (self.side1 * self.side2)


class Hexagon(Square):
    def __init__(self, side):
        super().__init__(side)

    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2) / 2


print("----Geometric object area calculator----".upper())
main = True
while main:
    print("Which shape would you like to calculate ?")
    print(
        """1 - Rectangle\n"""
        """2 - Square\n"""
        """3 - Triangle\n"""
        """4 - Circle\n"""
        """5 - Regular Hexagon\n"""
        """6 - Exit"""
    )

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                first_side = float(input("Enter first side of rectangle: "))
                second_side = float(input("Enter second side of rectangle: "))
                rectangle = Rectangle(first_side, second_side)
                print(rectangle.__str__())
            elif choice == 2:
                side = float(input("Enter side of square: "))
                square = Square(side)
                print(side.__str__())
            elif choice == 3:
                base = float(input("Enter base of triangle: "))
                height = float(input("Enter height of triangle: "))
                triangle = Triangle(base, height)
                print(triangle.__str__())
            elif choice == 4:
                radius = float(input("Enter radius of triangle: "))
                circle = Circle(radius)
                print(circle.__str__())
            elif choice == 5:
                side = float(input("Enter side of hexagon: "))
                hexagon = Hexagon(side)
                print(hexagon.__str__())
            elif choice == 6:
                main = False
                break
            break
        except ValueError:
            print("Please enter integer number.")
