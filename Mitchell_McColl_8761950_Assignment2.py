priceS = 0.0
hst = 0.0
amountS = 0
amountP = 0
final = 0.0
shirt = 0
pants = 0
colorP = 0
colorint = 0
senior = "i"
student = "i"
discount = 0.0
discountSType = "0%"
discountPType = "0%"
discountFinalP = 0.0
discountFinalS = 0.0

color = input("Please input what color of shirt you want: ")
while True:
    shirt = int(input("Please enter 1 for polo or 2 for t-shirt: "))

    if int(shirt) == 1:
        type = "polo shirts"
        break
    elif int(shirt) == 2:
        type = "t-shirts" 
        break
    else:
        print("Please enter either 1 or 2")  

amountS = int(input("Please enter the amount of shirts you want? Each shirt is $9.99: "))


while True:
    pants = int(input("Please enter 1 for pants or 2 for shorts: "))

    if int(pants) == 1:
        typeP = "pants"
        break
    elif int(pants) == 2:
        typeP = "shorts"
        break
    else:
        print("Please enter either 1 or 2")  

while True:
    colorint = input("Please enter the color of " + typeP + " you want. 1 for Blue, 2 for Red, or 3 for Black: ")
    if int(colorint) == 1:
        colorP = "blue"
        break
    elif int(colorint) == 2:
        colorP = "red"
        break
    elif int(colorint) == 3:
        colorP = "black"
        break
    else:
        print("Please enter either 1, 2, or 3")  

amountP = int(input("Please enter how many " + typeP + " do you want to buy? they are $5.50 each: "))

while True:
    student = input("Please enter Y if you are a student/senior or N if you are not: ")
    if student == "y" or student == "Y":
        discount = 0.10
        break
    elif student == "n" or student == "N":    
        break
    else:
        print("Please select Y for yes or N for no!")



priceS = float(amountS) * 9.99
priceP = float(amountP) * 5.50


if amountS >= 3:
    discountfinalS = priceS * 0.15
    discountSType = "15%"
else:
    if student == "y" or student == "Y":
        discountSType = "10%"
    discountfinalS = priceS * discount

if amountP >= 3:
    discountfinalP = priceP * 0.15
    discountPType = "15%"
else:
    if student == "y" or student == "Y":
        discountPType = "10%"
    discountfinalP = priceP * discount

finalS = priceS - discountfinalS
finalP = priceP - discountfinalP
finalS = round(finalS, 2)
finalP = round(finalP, 2)
hst = (finalS + finalP) * 0.13
final = finalS + hst
final = round(final, 2)

print("You bought a total of " + str(amountS) + " " + color + " " + type + " with a " + discountSType + " discount for a total price of $" + str(finalS) + " before tax!")
print("You also bought a total of " + str(amountP) + " " + colorP + " " + typeP + " with a " + discountPType + " discount for a total price of $" + str(finalP) + " before tax!")
print("Your final price after tax is $" + str(final))