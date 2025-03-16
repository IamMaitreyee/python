class Rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length * self.breadth)
if __name__ == "__main__":
    length = float(input("Enter the length of a rectangle: "))
    breadth = float(input("Enter the breadth of a rectangle: "))

    rect=Rectangle(length,breadth)
    print(f"Area of rectangle: {rect.area()}")
    print(f"Perimeter of rectangle: {rect.perimeter()}")


