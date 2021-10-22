class Student:

    school = "ACS/IT" #This is a class attribute

    def __init__(self, name, studentID):
        self.name = name #This is an instance attribute
        self.studentID = studentID #This is an attribute as well

    def description(self):
        return f"{self.name} has a student id of:  {self.studentID}"

    def grade(self,mark):
        return f"{self.name} has a mark of {mark}"

alice = Student("Alice McBride", 1234567)

print(alice.studentID, alice.name)
print(alice.description())