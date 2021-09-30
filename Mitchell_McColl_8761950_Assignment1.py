price = 0.0
hst = 0.0
amount = 0
final = 0.0
shirt = 0
print("This program will ask the user what color they want, what type of shirt they want, and the amount of shirts. The program will then calculate the amount of shirts with the price then calculate and add the HST to the final price\n\n")

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
