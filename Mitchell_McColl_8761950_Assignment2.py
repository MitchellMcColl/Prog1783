price = 0.0
hst = 0.0
amountS = 0
amountP = 0
final = 0.0
shirt = 0
pants = 0
colorS = 0
print("This program will ask the user what color they want, what type of shirt they want, and the amount of shirts. The program will then calculate the amount of shirts with the price then calculate and add the HST to the final price\n\n")

color = input("Please input what color of shirt you want: ")
shirt = input("Please enter 1 for polo or 2 for t-shirt: ")

while colorS != 1 or colorS != 2 or colorS != 3:
    colorS = int(input("Please enter the color of pants you want: 1 for Blue, 2 for Black, 3 for Red: "))
    if colorS != 1 or colorS != 2 or colorS != 3:
        print("Please choose either 1, 2, or 3")

pants = input("Please enter 1 for pants or 2 for shorts: ")

if int(shirt) == 1:
    type = "polo shirts"
elif int(shirt) == 2:
    type = "t-shirts"   
else:
    print("error")
    exit()
    

amountS = input("Please enter the amount of shirts you want? Each shirt is $9.99: ")
price = float(amount) * 9.99
hst = price * 0.13
final = hst + price
print("you bought " + amountS + " " + color + " " + type + " for a total price of $" + str(final))
