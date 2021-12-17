import datetime

class AnalyzeTriangle:
    def __init__(self, angle1, angle2, angle3, triangle, time):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.triangle = triangle
        self.time = time
    

    def validateTriangle(self):
        global triangle
       
        triangle = angle1 + angle2 + angle3
        if triangle == 180:
            print("Your angles form a triangle")
        else:
            print("Your angles do not form a triangle")
            print(time)
            exit()
        

        if angle1 == angle2 and angle2 == angle3 and angle3 == angle1:
            print("Your triangle is an Equilateral")
        elif angle1 == angle2 or angle2 == angle3 or angle3 == angle1:
            print("Your triangle is an Isoceles")
        else:
            print("Your Triangle is a Scalene")
        
        print(time)




angle1 = int(input("Please enter angle 1: "))
angle2 = int(input("Please enter angle 2: "))
angle3 = int(input("Please enter angle 3: "))
triangle = 0

t = datetime.datetime.now()
time = t.strftime("%m-%d-%Y, %Hh:%Mm:%Ss")

tri = AnalyzeTriangle(angle1, angle2, angle3, triangle, time)

tri.validateTriangle()
