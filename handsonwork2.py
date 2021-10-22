class CarType:
    def __init__(car, make, color, mileage, year):
        car.make = make
        car.color = color
        car.mileage = mileage
        car.year = year
        
        
    

    def mycar(car):
        return f"My car is a {car.make} with the color {car.color}, a mileage of {car.mileage}K, and from the year {car.year}"

make = input("Enter your cars make: ")
color = input("Enter your cars color: ")
mileage = input("Enter your cars mileage: ")
year = input("Enter your cars year: ")

mycar = CarType(make, color, mileage, year)
print(mycar.mycar())

