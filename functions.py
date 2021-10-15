def myFunction():
    print("Hello...PROG1783")

def Function2(firstname, age):
    print("Hello"+ firstname + "I belive you are " + age + " Years old.")

Function2("Alice", str(21))
Function2("Bob", str(25))
Function2("Charlie", str(27))

def areaOfCircle(radius):
    PI = 3.14
    area = PI + radius**2
    return area
a = int(input("Please enter a radius for the circle: "))
print(areaOfCircle(a))