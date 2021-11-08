num1 = 0.0
num2 = 0.0

def calculateNumbers(num1, num2):
    if num1 > num2:
            print("Your first number is greater than your second number!")
    elif num1 == num2:
            print("Your numbers are equal!")
    else:
            print("Your first number is less than your second number!")



num1 = input("Please enter your first number here: ")
num2 = input("Please enter your second number here: ")

calculateNumbers(num1, num2)

