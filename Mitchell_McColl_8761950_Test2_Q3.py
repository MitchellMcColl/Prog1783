class Account:
    def __init__(self, money):
        self.money = money
    
    def deposit(self):
        global money
        depo = 0.0
        depo = float(input("Please enter your deposit here: $"))
        money += depo
        return
    
    def withdraw(self):
        global money
        withd = 0.0
        withd = float(input("Please enter how much you wish to withdraw: $"))
        money -= withd
        return
    
    def balance(self):
        global money
        money = round(money, 2)
        print("Here is your balance: $" + str(money))
        return

money = 0.0
bal = Account(money)
choice = 0

bal.deposit()
bal.balance()

while True:
    choice = int(input("Please enter 1 for withdrawl or 2 for deposit: "))
    if choice == 1:
        bal.withdraw()
        break
    elif choice == 2:
        bal.deposit()
        break
    else:
        print("Please choose either 1 or 2")

bal.balance()
    

