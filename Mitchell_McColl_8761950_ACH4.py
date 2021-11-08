class Calculator:
    def __init__(self, num1, num2, final):
        self.num1 = num1
        self.num2 = num2
        self.final = final
    
    def addition(self):
        global num1, num2, final
        final = num1 + num2
    
    def subtraction(self):
        global num1, num2, final
        final = num1 - num2
    
    def multiplication(self):
        global num1, num2, final
        final = num1 * num2
    
    def division(self):
        global num1, num2, final
        final = num1 / num2
    
    def modulusDivision(self):
        global num1, num2, final
        final = num1 % num2

num1 = 0.0
num2 = 0.0
final = 0.0
choice = 0
calc = Calculator(num1, num2, final)

choice = int(input("Please enter \n1 for addition \n2 for subtraction \n3 for mulitplication \n4 for division \n5 for modulus: "))
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if choice == 1:
    calc.addition()
elif choice == 2:
    calc.subtraction()
elif choice == 3:
    calc.multiplication()
elif choice == 4:
    calc.division()
elif choice == 5:
    calc.modulusDivision()
else:
    print("Please choose between 1-5")


print("Your final number is: " + str(final))