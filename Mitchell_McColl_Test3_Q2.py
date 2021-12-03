class Rectangle:
    def __init__(self, length, width, area, perim):
        self.length = length
        self.width = width
        self.area = area
        self.perim = perim


    def getPerimeter(self):
        global length, width, perim
        perim = 2 * (length + width)
    

    def getArea(self):
        global length, width, area
        area = length * width
    
    
    def showResults(self):
        global perim, area
        print("The perimeter of your rectangle is: " + str(round(perim, 2)))
        print("The area of your rectangle is " + str(round(area, 2)))





length = float(input("Please enter the length of your rectangle here: "))
width = float(input("Please enter the width of your rectangle here: "))
area = 0.0
perim = 0.0
num = Rectangle(length, width, area, perim)

num.getPerimeter()
num.getArea()
num.showResults()