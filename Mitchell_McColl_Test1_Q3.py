class Temperatures:
    def __init__(self, temp1, temp2, temp3, average1, average2, average3):
        self.temp1 = temp1
        self.temp2 = temp2
        self.temp3 = temp3
        self.average1 = average1
        self.average2 = average2
        self.average3 = average3
    
    def enterTemp(self):
        print("Please enter 3 temperatures for Toronto: ")
        for i in range(3):
            x = float(input())
            temp1.append(x)

        print("Please enter 3 temperatures for London: ")
        for i in range(3):
            x = float(input())
            temp2.append(x)

        print("Please enter 3 temperatures for Owen Sound: ")
        for i in range(3):
            x = float(input())
            temp3.append(x)   
        return


    def calcAverageTemp(self):
        global average1, average2, average3
        average1 = float(sum(temp1)) / 3
        average1 = round(average1, 1)

        average2 = float(sum(temp2)) / 3
        average2 = round(average2, 1)

        average3 = float(sum(temp3)) / 3
        average3 = round(average3, 1)
        return



    def displayTemp(self):
        print("Your average temperature for Toronto is: " + str(average1))
        print("Your average temperature for London is: " + str(average2))
        print("Your average temperature for Owen Sound is: " + str(average3))
        return

temp1 = []
temp2 = []
temp3 = []
average1 = 0.0
average2 = 0.0
average3 = 0.0
temp = Temperatures(temp1, temp2, temp3, average1, average2, average3)

temp.enterTemp()
temp.calcAverageTemp()
temp.displayTemp()