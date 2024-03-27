"""
Inheritance is an importance concept in OOP
The main concept of OOP is encapsulation which is achieved by class

The intend of OOP is incomplete without the concept of Inheritance

"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)
class Student(Person):
    def __init__(self,r,name,age):
        super().__init__(name,age)
        self.roll = r
    def Rollnumber(self,r):
        self.roll = r
    def showroll(self):
        print(self.roll)
p1 = Student(211012,"Adarsh",19)
p1.showName()
p1.showAge()
p1.showroll()