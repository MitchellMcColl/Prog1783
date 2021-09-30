price = 0.0
hst = 0.0
amount = 0
final = 0.0
shirt = 0

color = input("Please input what color of shirt you want: ")
shirt = input("Please enter 1 for polo or 2 for t-shirt: ")

if int(shirt) == 1:
    type = "polo shirts"
elif int(shirt) == 2:
    type = "t-shirts"   
else:
    print("error")
    exit()
    


amount = input("Please enter the amount of shirts you want: ")
price = float(amount) * 9.99
hst = price * 0.13
final = hst + price
print("you bought " + amount + " " + color + " " + type + " for a total price of $" + str(final))
