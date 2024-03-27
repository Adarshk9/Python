class Student:
    def __init__(self):
        name = input("Enter Name")
        self.name = name
        roll = input("Enter roll number")
        self.rollno = roll
class Other(Student):
    def showData(self):
        print("Name = ",self.name)
        print("Roll Number = ",self.rollno)
obj = Other()
obj.showData()        