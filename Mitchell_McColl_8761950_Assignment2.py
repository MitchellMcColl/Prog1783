price = 0.0
hst = 0.0
amountS = 0
amountP = 0
final = 0.0
shirt = 0
pants = 0
colorP = 0
colorint = 0

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

amountS = input("Please enter the amount of shirts you want? Each shirt is $9.99: ")


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
    colorint = input("Please enter the color of " + typeP + " you want. 1 for Blue, 2 for Red, or 3 for Black")
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




price = float(amountS) * 9.99
hst = price * 0.13
final = hst + price
print("you bought " + amountS + " " + color + " " + type + " for a total price of $" + str(final))
