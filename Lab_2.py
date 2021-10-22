class Grades:
    def __init__(self, Mitchell, Bob, Suzie, John, students):
        self.Mitchell = Mitchell
        self.Bob = Bob
        self.Suzie = Suzie
        self.John = John
        self.students = students


    def enterGrades(self):
        for j in self.students:
            print(f"Enter your 5 grades for: {self.students[j]}")
            for i in range(5):
                self.students[j, i] = input()
                


    def displayGrades(self):
         for j in self.students:
            print(f"Your 5 grades for {self.students[j]} are: ")
            for i in range(4):
               print({self.students[j, i]})


Mitchell = [4]
Bob = [4]
Suzie = [4]
John = [4]
students = [Mitchell, Bob, Suzie, John]

mygrades = Grades(Mitchell, Bob, Suzie, John, students)
mygrades.enterGrades()
mygrades.displayGrades()  




